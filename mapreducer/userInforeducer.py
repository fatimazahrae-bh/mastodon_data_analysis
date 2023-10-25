#!/usr/bin/env python3

import sys
import json

current_user = None
total_followers_count = 0
total_reblogs_count = 0
user_created_at = None

for line in sys.stdin:
    try:
        user, data_json = line.strip().split('\t')
        data = json.loads(data_json)

        if current_user == user:
            total_followers_count += data['followers_count']
            total_reblogs_count += data['reblogs_count']
            if not user_created_at:
                user_created_at = data['created_at']
        else:
            if current_user:
                # Émettre le résultat pour l'utilisateur précédent
                result = {
                    'followers_count': total_followers_count,
                    'reblogs_count': total_reblogs_count,
                    'created_at': user_created_at
                }
                print(f"{current_user}\t{json.dumps(result)}")

            # Réinitialiser pour le nouvel utilisateur
            current_user = user
            total_followers_count = data['followers_count']
            total_reblogs_count = data['reblogs_count']
            user_created_at = data['created_at']

    except (ValueError, KeyError):
        # Ignorer les lignes mal formatées ou celles qui manquent de clés
        continue

if current_user:
    # Émettre le résultat pour le dernier utilisateur
    result = {
        'followers_count': total_followers_count,
        'reblogs_count': total_reblogs_count,
        'created_at': user_created_at
    }
    print(f"{current_user}\t{json.dumps(result)}")

