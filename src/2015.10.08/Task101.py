#!/usr/bin/python2
# -*- coding: utf-8 -*-

"""Rozwiązanie zadania 101."""

def uniq_elements(insequence):
    """Zwraca zwraca liczbę różnych elementów."""
    return len(set(insequence))

if __name__ == '__main__':
    print uniq_elements([1, 2, 3, 4, 4, 5])
