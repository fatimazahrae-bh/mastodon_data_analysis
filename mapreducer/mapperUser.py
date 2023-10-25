#!/usr/bin/env python3

import sys
import json

for line in sys.stdin:
    try:
        toot = json.loads(line)
        user = toot['account']
        username = user['username']
        followers_count = user['followers_count']
        reblogs_count = toot['reblogs_count']
        user_created_at = user['created_at']

        # Émettre un couple clé-valeur
        # La clé est l'identifiant de l'utilisateur
        # La valeur est un JSON contenant les informations pertinentes
        data = {
            'username': username,
            'followers_count': followers_count,
            'reblogs_count': reblogs_count,
            'user_created_at': user_created_at
        }
        print(f"{username}\t{json.dumps(data)}")
    except:
        pass

