#!/usr/bin/python2
# -*- coding: utf-8 -*-

import sys

MAP_COUNTER = {
	0 : "0",
	1 : "A",
	2 : "B",
	3 : "C",
	4 : "D",
	5 : "E",
	6 : "F",
	7 : "G",
	8 : "H",
	9 : "I",
	10 : "J",
	11 : "K",
	12 : "L",
	13 : "M",
	14 : "N",
	15 : "O",
	16 : "P",
	17 : "R",
	18 : "S",
	19 : "T",
	20 : "U",
	21 : "W",
	22 : "X",
	23 : "Y",
	24 : "Z",
	25 : "a",
	26 : "b",
	27 : "c",
	28 : "d",
	29 : "e",
	30 : "f",
	31 : "g",
	32 : "h",
	33 : "i",
	34 : "j",
	35 : "k",
	36 : "l",
	37 : "m",
	38 : "n",
	39 : "o",
	40 : "p",
	41 : "r",
	42 : "s",
	43 : "t",
	44 : "u",
	45 : "w",
	46 : "x",
	47 : "y",
	48 : "z"
}

LEN_WORD_0 = 0
LEN_WORD_1 = 0
OUTPUT = u""
LINES = dict()
BAD = 0

FILE_SAVE_IN = open("data/data_raw_in", "w")
FILE_SAVE_OUT = open("data/data_raw_out", "w")


for line in sys.stdin:
	line = line.rstrip()
	line = line.decode('utf-8')
	word = line.split()
	FILE_SAVE_IN.write(word[0].encode('utf-8') + "\t" + word[1].encode('utf-8') + "\n")
	LEN_WORD_0 = len(word[0])
	LEN_WORD_1 = len(word[1])
	OUTPUT = word[0] + u"+"
	if LEN_WORD_0 > 1 and word[1][0] != u"+":
		if (word[0][0:3] == u"nie" or word[0][0:3] == u"naj") and word[0][0] != word[1][0]:
			1
		else:
			if LEN_WORD_0 > LEN_WORD_1:
				for i in range(0,LEN_WORD_0):
					if i < LEN_WORD_1:
						if word[0][i] != word[1][i]:
							OUTPUT += MAP_COUNTER[LEN_WORD_0-i] + word[1][i:]
							break
					else:
						OUTPUT += MAP_COUNTER[LEN_WORD_0-i]
						break;
			elif LEN_WORD_0 == LEN_WORD_1:
				for i in range(0,LEN_WORD_0):
					if word[0][i] != word[1][i]:
						OUTPUT += MAP_COUNTER[LEN_WORD_0-i] + word[1][i:]
						break
				else:
					OUTPUT += u"0"
			else:
				for i in range(0,LEN_WORD_1):
					if i < LEN_WORD_0:
						if word[0][i] != word[1][i]:
							OUTPUT += MAP_COUNTER[LEN_WORD_0-i] + word[1][i:]
							break
					else:
						OUTPUT += MAP_COUNTER[LEN_WORD_0-i] + word[1][i:]
						break
			if OUTPUT not in LINES:
				LINES[OUTPUT] = 0
				# print OUTPUT.encode('utf-8')
				FILE_SAVE_OUT.write(OUTPUT.encode('utf-8') + "\n")
	"""
	print word[0].encode('utf-8')
	print word[1].encode('utf-8')
	print OUTPUT.encode('utf-8'), "\n"
	"""
FILE_SAVE_IN.close()
FILE_SAVE_OUT.close()
