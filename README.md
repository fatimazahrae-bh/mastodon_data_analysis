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

# Conformité au RGPD

Le Règlement général sur la protection des données (RGPD) est un ensemble de réglementations régissant la protection des données et la vie privée des individus au sein de l'Union européenne (UE). Lorsque vous travaillez avec des données, il est important de comprendre le RGPD et ses implications. Voici comment les considérations du RGPD s'appliquent aux données d'exemple :

## Données d'Exemple et RGPD

- **ID** : Le champ "id" représente généralement un identifiant unique pour un utilisateur ou une publication. Pour être conforme au RGPD, vous devez vous assurer que ces identifiants n'exposent pas d'informations personnelles sensibles sans le consentement approprié.

- **Créé le** : "created_at" indique quand le contenu a été créé. Assurez-vous de respecter les politiques de conservation des données du RGPD et de gérer de manière sécurisée les horodatages, en particulier s'ils incluent des données spécifiques à l'utilisateur.

- **Sensible** : Le champ "sensitive" suggère si le contenu est sensible. Vous devez traiter et protéger les données sensibles avec soin pour respecter la conformité au RGPD.

- **Texte Spoiler** : Bien que "spoiler_text" ne contienne peut-être pas de données personnelles, il est essentiel d'utiliser un chiffrement approprié et des contrôles d'accès s'il contient des informations sensibles.

- **Visibilité** : Le champ "visibility" détermine qui peut voir le contenu. Assurez-vous que les contrôles d'accès et les paramètres de confidentialité respectent les exigences du RGPD.

- **Langue** : "language" est un attribut du contenu. Assurez-vous que le contenu dans différentes langues respecte les réglementations spécifiques de la langue du RGPD, le cas échéant.

- **URI et URL** : Les URIs et les URL peuvent renvoyer vers des ressources externes. Assurez-vous d'obtenir le consentement approprié et de respecter les politiques de confidentialité du RGPD lors de la diffusion de liens, en tenant compte des implications du RGPD.

- **Compteur de Réponses, Repartages et Favoris** : Ces mesures ne doivent pas révéler d'informations sensibles spécifiques à l'utilisateur. Mettez en œuvre des mesures de confidentialité appropriées et l'agrégation des données si nécessaire.

- **Contenu** : Le champ "content" peut contenir du contenu généré par l'utilisateur. Les utilisateurs doivent consentir à la collecte et au stockage de leur contenu conformément aux exigences du RGPD.

- **Pièces Jointes Multimédias** : Gérez les pièces jointes multimédias de manière à ce qu'elles n'exposent pas d'informations sensibles sur les utilisateurs sans leur consentement approprié.

- **Mentions et Étiquettes** : Assurez-vous que les mentions et les étiquettes ne révèlent pas de données personnelles sans le consentement de l'utilisateur.

- **Données du Compte** : "account" inclut des informations de profil d'utilisateur. Traitez et sécurisez correctement ces informations pour respecter la confidentialité du RGPD.

## Conformité et Protection des Données

La conformité au RGPD est une responsabilité complexe, et il est essentiel de mettre en place des pratiques et des politiques de protection des données qui respectent les droits et la vie privée des individus. Recherchez toujours des conseils juridiques lors de la manipulation de données personnelles pour garantir la conformité au RGPD.

