#!/usr/bin/python2
# -*- coding: utf-8 -*-

"""Rozwiązanie zadania 103."""

def suffixes(instring):
    """Generuje wszystkie sufiksy z podanego stringa."""
    outsufiks = []
    for i in range(len(instring)):
        outsufiks.append(instring[i:])
    return outsufiks

if __name__ == '__main__':
    print suffixes("banana")
