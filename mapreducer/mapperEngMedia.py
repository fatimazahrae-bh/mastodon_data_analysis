#!/usr/bin/env python3

import sys
import json

for line in sys.stdin:
    try:
        toot = json.loads(line)
        media_attachments = toot.get('media_attachments', [])  # Extrait les pièces jointes multimédias

        # Vérifie si le toot a des pièces jointes multimédias
        has_media = 1 if len(media_attachments) > 0 else 0

        # Émet 1 si le toot a des pièces jointes multimédias, sinon émet 0
        print(f"{has_media}\t1")
    except:
        pass
