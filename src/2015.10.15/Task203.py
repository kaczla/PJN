#!/usr/bin/python2
# -*- coding: utf-8 -*-

"""Rozwiązanie zadania 203."""

import sys
import re


if len(sys.argv) >= 3:
    WORD = str(sys.argv[1])
    WORD_LEN = len(WORD)
    MAX_N = int(sys.argv[2])+1
else:
    MAX_N = 15
    WORD = "have"
    WORD_LEN = len(WORD)
for line in sys.stdin:
    a = [m.start() for m in re.finditer(WORD, line)]
    for i in a:
        print " ".join((
            line[i-MAX_N:i],
            line[i:i+WORD_LEN],
            line[i+WORD_LEN:i++WORD_LEN+MAX_N]
            ))
