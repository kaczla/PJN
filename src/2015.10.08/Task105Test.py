#!/usr/bin/python2
# -*- coding: utf-8 -*-

"""Zadanie 105

Napisz program do kodowania słów tekstu. Kodowanie powinno odbywać się
według następującej zasady - każdemu słowu jest przypisywana liczba
naturalna. Na przykład tekst: "to jest przykładowe zdanie a to jest
przykładowe sformułowanie" powinien być zakodowany jako:

[0, 1, 2, 3, 4, 0, 1, 2, 5]

Program powinien czytać tekst ze standardowego wejścia i pisać na
standardowe wyjście, natomiast główna funkcja powinna nazywać się
code_words.

NAME: code_words
PARAMS: string
RETURN: list
POINTS: 20

"""

import unittest
from Task105 import code_words

class Task105Test(unittest.TestCase):
    """Testy do zadania 105"""

    def test_main(self):
        """Główny test."""
        self.assertEqual(code_words("to jest przykładowe zdanie a to jest przykładowe sformułowanie"),
                         [0, 1, 2, 3, 4, 0, 1, 2, 5])

    def test_singleton(self):
        """Test na jednowyrazowym tekście."""
        self.assertEqual(code_words("one"), [0])

    def test_double(self):
        """Test na dwuwyrazowym tekście."""
        self.assertEqual(code_words("one two"), [0, 1])


if __name__ == '__main__':
    unittest.main()
