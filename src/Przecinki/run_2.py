#!/usr/bin/python2
# -*- coding: utf-8 -*-

"""Przewidywanie ilości samogłosego z zdaniu."""

import sys
from collections import defaultdict
import numpy as np
import matplotlib.pyplot as plt

if len(sys.argv) < 2:
    print "Arguments are empty!"
    sys.exit(0)

SENTENCES = defaultdict(list)
for line in sys.stdin:
    line = line.rstrip()
    words = line.split()
    i = line.count("a")
    i += line.count("ą")
    i += line.count("e")
    i += line.count("ę")
    i += line.count("i")
    i += line.count("o")
    i += line.count("u")
    i += line.count("ó")
    i += line.count("y")
    SENTENCES[len(words)].append(i);
    # if i > 0:
    #     SENTENCES[len(words)].append(i);

X = []
Y = []
X2 = []
Y2 = []
for key, value in SENTENCES.iteritems():
    if len(value) > 10:
        # print key, len(value), "=", float(sum(value))/float(len(value))
        X.append(key)
        Y.append(float(sum(value))/float(len(value)))
    for i in value:
        X2.append(key)
        Y2.append(i)

Z = np.polyfit(X, Y, 1)
P = np.poly1d(Z)
Z2 = np.polyfit(X2, Y2, 1)
P2 = np.poly1d(Z2)
XP = np.linspace(0, max(X2)+1)
plt.plot(X2,Y2,'.',X,Y,'o',XP,P(XP),'c--',XP,P2(XP),'r-')

FILE = open(sys.argv[1], "r")
CHECK_T = 0
CHECK_F = 0
for line in FILE:
    line = line.rstrip()
    x = len(line.split())
    y = line.count("a")
    y += line.count("ą")
    y += line.count("e")
    y += line.count("ę")
    y += line.count("i")
    y += line.count("o")
    y += line.count("u")
    y += line.count("ó")
    y += line.count("y")
    ans = P2(x)
    # print ans,";",x,"=",y
    if ans >= y-5 and ans <= y+5:
        CHECK_T += 1
    else:
        CHECK_F += 1
        # print "regression =",ans,"\tlen =",x,"\tcount =",y
print "All check:\t", CHECK_T+CHECK_F
print "TRUE:\t\t", CHECK_T
print "FALSE:\t\t", CHECK_F
print "ACCURACY:\t", round(float(CHECK_T)/float(CHECK_T+CHECK_F)*100, 2), "%"

plt.show()
