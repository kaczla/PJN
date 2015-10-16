#!/usr/bin/python2
# -*- coding: utf-8 -*-

"""Rozwiązanie zadania 100."""

def even_elements(inlist):
    """Zwraca elementy listy o indeksach parzystych."""
    return [inlist[i] for i in range(len(inlist)) if i % 2 == 0]

if __name__ == '__main__':
    print even_elements([1, 2, 3, 4])
