#!/usr/bin/env python
# -*- coding:utf-8 -*-
import sys,os
import math,re,datetime
#import MeCab

# name, basepath, list of texfiles
files = [
    ("ysuzuki","ysuzuki",["ysuzuki01.tex","ysuzuki02.tex","ysuzuki03.tex","ysuzuki04.tex","ysuzuki05.tex","ysuzuki_thesis.tex"]),
    ("naohiro_ito","naohiro_ito",["chapintro.tex","chapssd.tex","chaprelwork.tex","chapjoin.tex","chapmultiquery.tex","thesis.tex"]),
    ("y_maki","y_maki",["maki_01.tex","maki_02.tex","maki_03.tex","maki_04.tex","maki_05.tex","maki_06.tex","maki_07.tex","maki_thesis.tex"]),
    ("shimisho","shimisho",["sample.tex"]),
    ("tsan","senpai",["tsuchiyaALL.tex"]),
    ("nsan","senpai",["nishinaALL.tex"]),
    ("ssan","senpai",["suzukiALL.tex"]),
    ("ksan","senpai",["kuriharaALL.tex"]),
    ("osan","senpai",["okamotoALL.tex"])
         ]

#m = MeCab.Tagger()

now = datetime.datetime.today().strftime("%Y-%m-%d %H:%M")
sys.stderr.write("datetime" + "\t" + "\t".join([fi[0] for fi in files]) + "\n")
#print "datetime" + "\t" + "\t".join([fi[0] for fi in files])

output = [now]
for (author,basepath,texfiles) in files:
    wordCnt = 0
    lineCnt = 0
    for texfile in texfiles:
        #sys.stderr.write(texfile+"\n")
        f = open(basepath + "/" + texfile)
        for line in f:
            #print line.strip()

            try:
                if author == "y_maki":
                    line = line.decode("shift-jis").strip()
                else:
                    line = line.decode("utf8").strip()
            except:
                line = ""

            if len(line) == 0: 
               continue

            #コメントとoptionはカウントしない!
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
