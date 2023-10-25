
import happybase
from hdfs import InsecureClient
import sys

# HBase connection parameters
hbase_host = 'localhost'  # HBase host
hbase_port = 9090       # HBase port
hbase_table_name = 'tag_mention'  # Remplacez par le nom de votre table HBase

# HDFS client
hdfs_url = 'http://localhost:9870'
hdfs_client = InsecureClient(hdfs_url, user='hadoop')

# Chemin vers la sortie du reducer
output_file_path = "/Mostodon/Raw/tagMentionOutput/part-00000"

# Connexion à HBase
connection = happybase.Connection(hbase_host, hbase_port)

# Sélection de la table HBase
table = connection.table(hbase_table_name)

# Lecture de la sortie du reducer depuis HDFS
with hdfs_client.read(output_file_path) as reader:
    for line in reader:
        line = line.decode('utf-8')  # Décodage de la ligne en utilisant l'encodage UTF-8
        entity, count = line.strip().split('\t')

        # Insérer les données dans la table HBase
        table.put(entity.encode('utf-8'), {'cf:count': str(count).encode('utf-8')})

# Fermeture de la connexion à HBase
connection.close()

