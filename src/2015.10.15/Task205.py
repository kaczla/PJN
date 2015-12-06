#!/usr/bin/python2
# -*- coding: utf-8 -*-

import sys, re
from collections import defaultdict
def diac():
    lettermap = {'ą':'a', 'ć':'c', 'ę':'e', 'ł':'l', 'ń':'n', 'ó':'o', 'ś':'s', 'ź':'z', 'ż':'z', 'Ą':'A', 'Ć':'C', 'Ę':'E', 'Ł':'L', 'Ń':'N', 'Ó':'O', 'Ś':'S', 'Ź':'Z', 'Ż':'Z'}
    dictionary = defaultdict(set)
    words = re.findall(r'[ąćęłńóśźżĄĆĘŁŃÓŚŹŻ\w-]+', ' '.join(sys.stdin.readlines()))
    for word in words:
        norm_word = ''
        for i in range(len(word)):
            if word[i:i+2] in lettermap:
                norm_word += lettermap[word[i:i+2]]
            elif word[i-1:i+1] not in lettermap:
                norm_word += word[i]
        dictionary[norm_word].add(word)
    for key in sorted(dictionary):
        if len(dictionary[key]) > 1:
            print ' '.join(sorted(dictionary[key]))


if __name__ == '__main__':
    diac()
