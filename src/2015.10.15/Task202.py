#!/usr/bin/python2
# -*- coding: utf-8 -*-

"""Rozwiązanie zadania 202."""

import sys
import re

WORDS_RE = re.compile(r"\w+")
if len(sys.argv) > 1:
    MAX_N = int(sys.argv[1])
else:
    MAX_N = 3
for line in sys.stdin:
    words = []
    for i in WORDS_RE.findall(line):
        if i not in words:
            words.append(i)
    for i in range(0, len(words)-MAX_N+1):
        print " ".join(words[j] for j in range(i, i+MAX_N))
