#!/usr/bin/python2
# -*- coding: utf-8 -*-

"""Rozwiązanie zadania 104."""

def bigrams(instring):
    """Generuje wszystkie bigramy z elementów dla
    dowolnego typu sekwencyjnego w postaci listy."""
    bigram = []
    for i in range(0, len(instring)-1):
        bigram.append(instring[i:i+2])
    return bigram

if __name__ == '__main__':
    print bigrams("banana")
