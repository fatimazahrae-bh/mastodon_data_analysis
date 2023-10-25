import happybase
import sys
import json

# Paramètres de connexion HBase
hbase_host = '127.0.0.1'  # Adresse IP du serveur HBase
hbase_port = 9090       # Port HBase
hbase_table_name = 'userInfo'

# Se connecter à HBase
connection = happybase.Connection(hbase_host, hbase_port)

# Sélectionner la table HBase
table = connection.table(hbase_table_name)

# Traiter les données d'entrée du reducer
for line in sys.stdin:
    try:
        parts = line.strip().split('\t')
        if len(parts) == 2:
            user, data_json = parts
            data = json.loads(data_json)

            # Insérer les données dans la table HBase
            table.put(user.encode('utf-8'), {
                'cf:followers_count': str(data['followers_count']).encode('utf-8'),
                'cf:reblogs_count': str(data['reblogs_count']).encode('utf-8'),
                'cf:created_at': data['created_at'].encode('utf-8')
            })
        else:
            # Gérer les lignes mal formatées
            print(f"Ignorer la ligne mal formatée : {line}")

    except Exception as e:
        # Gérer les erreurs si nécessaire
        print(f"Erreur lors de l'insertion des données : {str(e)}")

# Fermer la connexion à HBase
connection.close()

