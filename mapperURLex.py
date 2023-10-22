#!/usr/bin/env python3

import sys
import json
import re

# Utilise une expression régulière pour extraire les URL des toots
url_pattern = re.compile(r'https?://[^\s]+')

for line in sys.stdin:
    try:
        toot = json.loads(line)
        content = toot.get('content', '')  # Extrait le contenu du toot
        urls = re.findall(url_pattern, content)  # Trouve toutes les URL dans le contenu
        
        for url in urls:
            # Émet chaque URL comme clé avec une valeur de 1
            print(f"{url}\t1")
    except:
        pass
