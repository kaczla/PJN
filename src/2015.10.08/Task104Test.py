#!/usr/bin/python2
# -*- coding: utf-8 -*-

"""
Zadanie 104

Napisz funkcję bigrams(sequence), która generuje wszystkie bigramy z
elementów dla dowolnego typu sekwencyjnego w postaci listy. Bigramem
nazywamy ciągi występujących po sobie elementów długości 2. Np. dla
"banana" wynikiem jest:

["ba", "an", "na", "an", "na"]

NAME: bigrams
PARAMS: string
RETURN: list
POINTS: 10

"""

import unittest
from Task104 import bigrams

class Task104Test(unittest.TestCase):
    """Testy do zadania 104"""

    def test_simple(self):
        """Prosty test."""
        self.assertEqual(bigrams("banana"), ["ba", "an", "na", "an", "na"])

    def test_double(self):
        """Test na dwuznakowym napisie."""
        self.assertEqual(bigrams("xy"), ["xy"])

    def test_triple(self):
        """Test na trzyznakowym napisie."""
        self.assertEqual(bigrams("xyz"), ["xy", "yz"])


if __name__ == '__main__':
    unittest.main()
