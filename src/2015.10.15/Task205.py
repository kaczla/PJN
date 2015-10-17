#!/usr/bin/python2
# -*- coding: utf-8 -*-

"""Rozwiązanie zadania 205."""

import sys
import re


for line in sys.stdin:
    a = [m.start() for m in re.finditer(WORD, line)]
    for i in a:
        print " ".join((
            line[i-MAX_N:i],
            line[i:i+WORD_LEN],
            line[i+WORD_LEN:i++WORD_LEN+MAX_N]
            ))
