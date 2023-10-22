#!/usr/bin/env python3

import sys

current_entity = None
current_count = 0

for line in sys.stdin:
    entity, count = line.strip().split('\t')

    if current_entity == entity:
        current_count += int(count)
    else:
        if current_entity:
            print(f"{current_entity}\t{current_count}")
        current_entity = entity
        current_count = int(count)

if current_entity:
    print(f"{current_entity}\t{current_count}")
