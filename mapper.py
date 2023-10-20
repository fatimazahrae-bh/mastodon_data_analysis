#!/usr/bin/env python3

import sys
import json

for line in sys.stdin:
    try:
        toot = json.loads(line)
        user = toot['account']
        username = user['username']
        followers_count = user['followers_count']
        print(f"{username}\t{followers_count}")
    except:
        pass
