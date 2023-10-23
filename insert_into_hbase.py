#!/usr/bin/env python3


#import happybase


# Chemin vers votre fichier de sortie
#output_file_path = "/Mostodon/Raw/dataoutput/part-00000"

# Ouvrez une connexion à HBase
#connection = happybase.Connection('127.0.0.1', 16010)

# Sélectionnez la table
#table = connection.table('table_utilisateurs')

# Ouvrez le fichier de sortie
#with open(output_file_path, "r") as output_file:
 #   for line in output_file:
  #      parts = line.strip().split("\t")
   #     if len(parts) == 2:
    #        username, followers_count = parts
            # Insérez les données dans HBase
     #       table.put(username, {"informations:followers_count": followers_count})

# Fermez la connexion
#connection.close()


import happybase
from hdfs import InsecureClient

# HBase connection parameters
hbase_host = '127.0.0.1'  # HBase host
hbase_port = 16010       # HBase port
hbase_table_name = 'table_utilisateurs'

# HDFS client
hdfs_url = 'http://localhost:9870'
hdfs_client = InsecureClient(hdfs_url, user='hadoop')

# Path to reduce output
#hdfs_file_path = '/output/ReducerResults1/part-00000'
output_file_path = "/Mostodon/Raw/dataoutput/part-00000"

# Connect to HBase
connection = happybase.Connection(hbase_host, hbase_port)

# Select the HBase table
table = connection.table(hbase_table_name)

# Read the reducer output from HDFS
with hdfs_client.read(output_file_path) as reader:
    for line in reader:
        line = line.decode('utf-8')  # Décodez la ligne en utilisant l'encodage UTF-8
        parts = line.strip().split("\t")
        if len(parts) == 2:
            username, followers_count = parts
            # Insert the data into HBase
            table.put(username, {"informations:followers_count": followers_count})



# Close the HBase connection
connection.close()



