#!/usr/bin/python2
# -*- coding: utf-8 -*-

"""Rozwiązanie zadania 204."""

import sys
import re

WORDS = {}
WORDS_RE = re.compile(r"[A-Za-z]+")
for line in sys.stdin:
    for i in WORDS_RE.findall(line):
        for j in i:
            if j not in WORDS:
                WORDS[j] = 1
            else:
                WORDS[j] += 1
for i in sorted(WORDS):
    print "%s\t%d" % (i, WORDS[i])
