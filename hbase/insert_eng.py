
import happybase
from hdfs import InsecureClient
import sys

# HBase connection parameters
hbase_host = 'localhost'  # HBase host
hbase_port = 9090       # HBase port
hbase_table_name = 'user_engagement'  # Le nom de votre table HBase pour l'engagement des utilisateurs

# HDFS client
hdfs_url = 'http://localhost:9870'
hdfs_client = InsecureClient(hdfs_url, user='hadoop')

# Path to reducer output in HDFS
output_file_path = "/Mostodon/Raw/userEn/part-00000"

# Connect to HBase
connection = happybase.Connection(hbase_host, hbase_port)

# Select the HBase table
table = connection.table(hbase_table_name)

# Read the reducer output from HDFS
with hdfs_client.read(output_file_path) as reader:
    for line in reader:
        line = line.decode('utf-8')  
        username, engagement = line.strip().split('\t')

        # Insérer les données dans la table HBase
        table.put(username.encode('utf-8'), {'cf:engagement': str(engagement).encode('utf-8')})

# Close the HBase connection
connection.close()
