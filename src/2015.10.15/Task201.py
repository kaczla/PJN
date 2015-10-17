#!/usr/bin/python2
# -*- coding: utf-8 -*-

"""Rozwiązanie zadania 201."""

import sys
import re

WORDS_RE = re.compile(r"\w+")
WORDS = {}
for line in sys.stdin:
    line = line.lower()
    for i in WORDS_RE.findall(line):
        if i not in WORDS:
            WORDS[i] = 1
        else:
            WORDS[i] += 1
for i in sorted(WORDS, key=WORDS.get, reverse=True):
    print "%d\t%s" % (WORDS.get(i), i)
