#!/usr/bin/env python
# -*- coding:utf-8 -*-
import sys,os
#import math,re,datetime

f = open("/home/ari/www/arieee.net/public_html/shuron/data")
data = {"cols":[{"type":"string","label":"datetime"}],"rows":[]}

# column
columns = f.readline().strip().split("\t")
for column in columns[1:]:
    data["cols"].append({"type":"number","label":column})

# row data    
for line in f:
    items = line.strip().split("\t")
    dataList = []
    dataList.append({"v":items[0]}) #datetime
    for item in items[1:]:
        dataList.append({"v":int(item)})

    data["rows"].append({"c":dataList})

import json
print json.dumps(data, sort_keys=True, indent=4)

