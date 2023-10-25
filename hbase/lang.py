#!/usr/bin/env python3

import sys
import json

for line in sys.stdin:
    try:
        toot = json.loads(line)
        language = toot.get('language', 'unknown')  # Extrait la langue du toot
        
        # Émet la langue comme clé avec une valeur de 1
        print(f"{language}\t1")
    except:
        pass
