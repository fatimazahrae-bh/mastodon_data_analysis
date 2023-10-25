import happybase
from hdfs import InsecureClient
import sys

# HBase connection parameters
hbase_host = 'localhost'  # HBase host
hbase_port = 9090       # HBase port
hbase_table_name = 'user_followers'  # Le nom de votre table HBase pour les followers

# HDFS client
hdfs_url = 'http://localhost:9870'
hdfs_client = InsecureClient(hdfs_url, user='hadoop')

# Path to TSV data in HDFS
tsv_file_path = "/Mostodon/Raw/userF/part-00000"

# Connect to HBase
connection = happybase.Connection(hbase_host, hbase_port)

# Select the HBase table
table = connection.table(hbase_table_name)

# Read the TSV data from HDFS
with hdfs_client.read(tsv_file_path) as reader:
    for line in reader:
        line = line.decode('utf-8')  
        parts = line.strip().split('\t')

        if len(parts) == 2:
            username, followers_count = parts
            # Insérer les données dans la table HBase
            table.put(username.encode('utf-8'), {'cf:followers_count': str(followers_count).encode('utf-8')})

# Close the HBase connection
connection.close()
