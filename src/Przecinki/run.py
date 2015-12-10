#!/usr/bin/python2
# -*- coding: utf-8 -*-

"""Przewidywanie ilości wystąpień przecinków z zdaniu."""

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
    i = line.count(",")
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
# plt.show()

FILE = open(sys.argv[1], "r")
CHECK_T = 0
CHECK_F = 0
for line in FILE:
    line = line.rstrip()
    x = len(line.split())
    y = float(line.count(","))
    ans = P2(x)
    # print ans,";",x,"=",y
    if ans >= y-1 and ans <= y+1:
        CHECK_T += 1
    else:
        CHECK_F += 1
        print "regression =",ans,"\tlen =",x,"\tcount =",y
print "All check:", CHECK_T+CHECK_F
print "TRUE:", CHECK_T
print "FALSE:", CHECK_F
