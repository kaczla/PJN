#!/usr/bin/python2
# -*- coding: utf-8 -*-

"""Rozwiązanie zadania 105."""

def code_words(instring):
    """Program do kodowania słów tekstu."""
    dictionary = {}
    number = 0
    for i in instring.split():
        if i not in dictionary:
            dictionary[i] = number
            number = number + 1
    for i in sorted(dictionary, key=len, reverse=True):
        instring = instring.replace(i, str(dictionary[i]))
    return [int(i) for i in instring.split()]

if __name__ == '__main__':
    print code_words("to jest przykład zdanie a to jest przykład sformułowanie")
