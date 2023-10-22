#!/usr/bin/env python3

import sys
import json

for line in sys.stdin:
    try:
        toot = json.loads(line)
        user = toot['account']
        created_at = user['created_at']
        
        # Extraire l'année de création de l'utilisateur
        user_year = created_at.split("-")[0]
        
        # Émettre l'année comme clé avec une valeur de 1
        print(f"{user_year}\t1")
    except:
        pass
