#!/usr/bin/python2
# -*- coding: utf-8 -*-

import sys

FILE_SAVE_OUT = open("data/symbols.txt", "w")

A = []

for line in sys.stdin:
	line = line.rstrip()
	line = line.decode('utf-8')
	LEN_WORD = len(line)
	for i in line:
		if i not in A:
			A.append(i)

COUNTER = 0
for i in sorted(A):
	FILE_SAVE_OUT.write(i.encode('utf-8') + " " + str(COUNTER) + "\n")
	COUNTER += 1

FILE_SAVE_OUT.close()
