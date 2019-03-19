#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import re
import sys

#debug = 100
debug = 0

if debug:
    dcount = 0

infn = sys.argv[1]
oufn = sys.argv[2]

tab = "\t"
Tags = {"javascript" : "1", "java" : "2", "python" : "3", "ruby" : "4",
"php" : "5", "c++" : "6", "c#" : "7", "go" : "8", "scala" : "9",
"swift" : "10"}

infd = open(infn, "r")
oufd = open(oufn, "w")
istr = infd.readline()
while istr:
    ntabs = istr.count(tab)
    if debug:
        dcount += 1
    if ntabs == 1:
        tp = istr.split(tab)
        qst = tp[0]
        tgs = tp[1].replace("\n","")
        tp = re.split('\s+', tgs)

        nmatches = 0
        matched = ""
        for i in tp:
            if i in Tags:
                nmatches += 1
                if nmatches > 1:
                    if debug:
                        print("ManyMatches: ", end="")
                        print(tp, end="")
                        print(" | " + qst)
                    break
                mTag = i
        if nmatches == 1:
            nqst = qst.strip()
            if nqst.find(":") != -1:
                gst = nqst.replace(":", "")
            if qst.find("|") != -1:
                ngst = qst.replace("|", "")
            oufd.write(Tags[mTag] + " | " + nqst + "\n")
            if debug:
                print(Tags[mTag] + " (" + mTag + ") | " + nqst)

    if debug and dcount >= debug:
        break
    istr = infd.readline()
infd.close()
oufd.close()