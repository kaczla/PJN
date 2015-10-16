#!/usr/bin/python2
# -*- coding: utf-8 -*-

"""Zadanie 103

NapNapisz funkcję suffixes(string), która generuje wszystkie sufiksy z
podanego stringa. Na przykład, dla stringa "banana" powinna zwrócić
listę:

["banana", "anana", "nana", "ana", "na", "a"]

NAME: suffixes
PARAMS: string
RETURN: list
POINTS: 10

"""

import unittest
from Task103 import suffixes

class Task103Test(unittest.TestCase):
    """Testy do zadania 103"""

    def test_simple(self):
        """Prosty test."""
        self.assertEqual(suffixes("banana"), ["banana", "anana", "nana", "ana", "na", "a"])

    def test_singleton(self):
        """Test na jednoznakowym napisie."""
        self.assertEqual(suffixes("x"), ["x"])

if __name__ == '__main__':
    unittest.main()
