import happybase
from hdfs import InsecureClient
import sys

# HBase connection parameters
hbase_host = 'localhost'  # HBase host
hbase_port = 9090       # HBase port
hbase_table_name = 'media'  # Remplacez par le nom de votre table HBase

# HDFS client
hdfs_url = 'http://localhost:9870'
hdfs_client = InsecureClient(hdfs_url, user='hadoop')

# Path to reduce output
output_file_path = "/Mostodon/Raw/EngMediaOutput1/part-00000"  # Chemin vers le fichier de sortie du reducer "engMediaOutput"

# Connect to HBase
connection = happybase.Connection(hbase_host, hbase_port)

# Select the HBase table
table = connection.table(hbase_table_name)

# Read the reducer output from HDFS
with hdfs_client.read(output_file_path) as reader:
    for line in reader:
        line = line.decode('utf-8')  # Décodez la ligne en utilisant l'encodage UTF-8
        has_media, count = line.strip().split('\t')

        # Insérer les données dans la table HBase
        # Vous pouvez utiliser la colonne 'cf:has_media' pour stocker la valeur de 'has_media' et 'cf:toot_count' pour stocker la valeur de 'count'.
        table.put(b'row_key', {b'cf:has_media': has_media.encode('utf-8'), b'cf:toot_count': count.encode('utf-8')})

# Close the HBase connection
connection.close()

