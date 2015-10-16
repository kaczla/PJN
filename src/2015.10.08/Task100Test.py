#!/usr/bin/python2
# -*- coding: utf-8 -*-

"""
Zadanie 100

Napisz funkcję `even_elements` zwracającą listę, która zawiera tylko
elementy z `list` o parzystych indeksach. (Zadanie kontrolne z gotowym
rozwiązaniem!)

NAME: even_elements
PARAMS: list
RETURN: list
POINTS: 0
"""

import unittest
from Task100 import even_elements

class Task100Test(unittest.TestCase):
    """Testy do zadania 100"""

    def test_sequence(self):
        """Prosty test."""
        self.assertEqual(even_elements([1, 2, 3, 4, 5, 6]), [1, 3, 5])

    def test_empty(self):
        """Test na pustej liście."""
        self.assertEqual(even_elements([]), [])

    def test_singleton(self):
        """Test na liście jednoelementowej."""
        self.assertEqual(even_elements([41]), [41])

    def test_two_elements(self):
        """Test na liście dwuelementowej."""
        self.assertEqual(even_elements([100, 2]), [100])

    def test_negatives(self):
        """Test na liście z ujemnym elementem."""
        self.assertEqual(even_elements([-31, 0, 2]), [-31, 2])

if __name__ == '__main__':
    unittest.main()
