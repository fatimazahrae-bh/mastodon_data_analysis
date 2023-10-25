import happybase
from hdfs import InsecureClient
import sys

# HBase connection parameters
hbase_host = 'localhost'  # HBase host
hbase_port = 9090       # HBase port
hbase_table_name = 'createdAt'  

# HDFS client
hdfs_url = 'http://localhost:9870'
hdfs_client = InsecureClient(hdfs_url, user='hadoop')

# Path to reducer output in HDFS
output_file_path = "/Mostodon/Raw/createdAt/part-00000"

# Connect to HBase
connection = happybase.Connection(hbase_host, hbase_port)

# Select the HBase table
table = connection.table(hbase_table_name)

# Read the reducer output from HDFS
with hdfs_client.read(output_file_path) as reader:
    for line in reader:
        line = line.decode('utf-8')  # Décodez la ligne en utilisant l'encodage UTF-8
        try:
            date, count = line.strip().split('\t')
            # Convertissez la chaîne en entier pour l'insertion
            count = int(count)
            # Insérez les données dans la table HBase
            table.put(date.encode('utf-8'), {'cf:count': str(count).encode('utf-8')})
        except ValueError:
            # Ignorez les lignes sans le format attendu
            continue

# Fermez la connexion à HBase
connection.close()
