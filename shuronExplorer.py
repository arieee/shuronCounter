#!/usr/bin/env python
# -*- coding:utf-8 -*-
import sys,os
import math,re,datetime
#import MeCab

files = [
    ("ysuzuki","ysuzuki/suzukiMasterThesis.tex"),
    ("naohiro_ito","naohiro_ito/thesis.tex"),
    ("y_maki","y_maki/sample.tex"),
    ("shimisho","shimisho/sample.tex"),
    ("tsan","senpai/tsuchiyaALL.tex"),
    ("nsan","senpai/nishinaALL.tex"),
    ("ssan","senpai/suzukiALL.tex"),
    ("ksan","senpai/kuriharaALL.tex"),
    ("osan","senpai/okamotoALL.tex")
         ]

#m = MeCab.Tagger()

now = datetime.datetime.today().strftime("%Y-%m-%d %H:%M")
sys.stderr.write("datetime" + "\t" + "\t".join([fi[0] for fi in files]) + "\n")
#print "datetime" + "\t" + "\t".join([fi[0] for fi in files])

output = [now]
for (author,path) in files:
    f = open(path)
    wordCnt = 0
    lineCnt = 0
    for line in f:
        #print line.strip()

        line = line.decode("utf8").strip()
        if len(line) == 0:
            continue

        if line[0] in u"\\%{}[]":
            #print "OUT!!!"
            continue #option系は飛ばす

        lineCnt += 1
        wordCnt += len(line)
        #print lineCnt,wordCnt
        
    #print now + "\t" + author + "\t" + str(lineCnt) + "\t" + str(wordCnt)
    output.append(str(wordCnt))

sys.stderr.write("\t".join(output)+"\n")
print "\t".join(output)
