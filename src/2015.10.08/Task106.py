#!/usr/bin/python2
# -*- coding: utf-8 -*-

"""Rozwiązanie zadania 106."""


def replace_words(instring, infile):
    """Zastępowanie wyrazów w tekście według słownika zdefiniowanego w pliku"""
    file_ = open(infile, 'r')
    line = file_.readlines()
    file_.close()
    dictionary = {}
    for i in line:
        if i.split()[0] not in dictionary:
            dictionary[i.split()[0]] = i.split()[1]
    for i in sorted(dictionary, key=len, reverse=True):
        instring = instring.replace(i, str(dictionary[i]))
    return instring

if __name__ == '__main__':
    print replace_words("Ala ma kota i psa", "Task106Test.dat")
