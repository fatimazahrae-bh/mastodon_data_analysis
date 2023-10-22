#!/usr/bin/env python3

import sys
import json

for line in sys.stdin:
    try:
        toot = json.loads(line)
        user = toot['account']
        username = user['username']
        reblogs_count = toot['reblogs_count']  # Nombre de reblogs
        print(f"{username}\t{reblogs_count}")
    except:
        pass
