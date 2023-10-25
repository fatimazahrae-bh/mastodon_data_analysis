import happybase
from hdfs import InsecureClient
import sys

# HBase connection parameters
hbase_host = 'localhost'  # HBase host
hbase_port = 9090       # HBase port
hbase_table_name = 'table_de_partage'

# HDFS client
hdfs_url = 'http://localhost:9870'
hdfs_client = InsecureClient(hdfs_url, user='hadoop')

# Path to reduce output
#hdfs_file_path = '/output/ReducerResults1/part-00000'
output_file_path = "/Mostodon/Raw/urlExternOutput/part-00000"

# Connect to HBase
connection = happybase.Connection(hbase_host, hbase_port)

# Select the HBase table
table = connection.table(hbase_table_name)

# Read the reducer output from HDFS
with hdfs_client.read(output_file_path) as reader:
    for line in reader:
        line = line.decode('utf-8')  # Décodez la ligne en utilisant l'encodage UTF-8
        url, share_count = line.strip().split('\t')

        # Insérer les données dans la table HBase
        table.put(url.encode('utf-8'), {'cf:share_count': str(share_count).encode('utf-8')})

# Close the HBase connection
connection.close()

