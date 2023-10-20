# mastodon_data_analysis

Ce projet a pour but de collecter des données à partir d'une instance Mastodon à l'aide d'un script Python. Les données collectées sont ensuite transformées et stockées dans le système de fichiers distribués Hadoop HDFS. Les données collectées comprennent des toots (messages) publics et diverses informations associées.

### Fonctionnalités principales :
- Collecte de toots depuis une instance Mastodon via son API publique.
- Transformation et nettoyage des données pour une utilisation ultérieure.
- Stockage des données nettoyées dans HDFS pour le traitement Big Data.
- Traitement ultérieur des données à l'aide de MapReduce.
- Affichage du nombre de followers pour chaque utilisateur (username).

### Configuration requise :
- Python 3.x pour le script de collecte.
- Hadoop HDFS pour le stockage et le traitement des données.
- Une instance Mastodon accessible pour collecter les données.

### Utilisation :
1. Exécutez le script Python de collecte pour collecter les données depuis l'instance Mastodon.
2. Stockez les données nettoyées dans HDFS.
3. Utilisez MapReduce pour traiter les données stockées.

Ce projet est conçu pour illustrer un flux de travail typique de collecte, de stockage et de traitement de données à grande échelle à l'aide d'outils populaires tels que Mastodon, Python, Hadoop et MapReduce.
