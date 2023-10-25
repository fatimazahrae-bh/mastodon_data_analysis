from mastodon import Mastodon
import json
import datetime
from hdfs import InsecureClient




def serialize_datetime(obj):
    if isinstance(obj, datetime.datetime):
        return obj.isoformat()
    raise TypeError("Type not serializable")


mastodon = Mastodon(
    client_id='TKemtCd4jw5vcGeSoM_d2RtjzDDcQW3Y5ZdT7cSyrlI',
    client_secret='_AnfHXoVq03Z8l9Ob_U7cE9dFc-L_kGg3uI8HCFhV8M',
    access_token='VvqdDjGlhxY1oK5sCUQ3m_hX-cin-acO9OMWqm6TINc',
    api_base_url='https://mastodon.social/'
)




try:
    with open('last_toot_id.txt', 'r') as f:
        last_toot_id = f.read().strip()
except FileNotFoundError:
    last_toot_id = None


public_posts = mastodon.timeline_public(limit=40, since_id=last_toot_id)


toot_data = []


for toot in public_posts:
    try:
        toot_data.append(toot)
    except Exception as e:
        print(f"Error processing toot: {e}")


json_data = json.dumps(toot_data, indent=4, default=serialize_datetime)




# Écrivez les données JSON dans un fichier
with open('toots_data.json', 'w') as json_file:
    json.dump(toot_data, json_file, default=serialize_datetime, indent=4)




# Encode the JSON string as bytes
json_bytes = json_data.encode('utf-8')


with open("toots_data.json", "w") as outfile:
    outfile.write(json_data)




#  define location
hdfs_destination_path = '/mastodon/toots_data.json'


# Create an HDFS client
hdfs_client = InsecureClient('http://localhost:9870/', user='hadoop')


with hdfs_client.write(hdfs_destination_path, overwrite=True) as writer:
    writer.write(json_bytes)


print(f"Data written to HDFS at: {hdfs_destination_path}")
