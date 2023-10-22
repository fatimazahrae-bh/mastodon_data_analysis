#!/usr/bin/env python3

import sys
import json

for line in sys.stdin:
    try:
        toot = json.loads(line)
        post_id = toot['id']
        
        # Extraction des balises (hashtags)
        hashtags = toot['tags']
        for hashtag in hashtags:
            print(f"{hashtag}\t1")

        # Extraction des utilisateurs mentionnés
        mentions = toot['mentions']
        for mention in mentions:
            print(f"{mention}\t1")
    except:
        pass
