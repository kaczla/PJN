#!/usr/bin/python2
# -*- coding: utf-8 -*-

"""Rozwiązanie zadania 102."""

def freq_dic(insequence):
    """Zwraca liczbę wystąpień elementów dla dowolnego typu sekwencyjnego."""
    cout_letter = {}
    for i in set(insequence):
        cout_letter[i] = insequence.count(i)
    return cout_letter

if __name__ == '__main__':
    print freq_dic("abracadabra")
