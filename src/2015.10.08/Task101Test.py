#!/usr/bin/python2
# -*- coding: utf-8 -*-

"""
Zadanie 101

Napisz funkcję uniq_elements(sequence), która dla dowolnego typu
sekwencyjnego (krotka, lista, łańcuch, zbiór) zwraca liczbę różnych
elementów. Np. dla łańcucha "abracadabra" wynik jest równy 5.

NAME: uniq_elements
PARAMS: sequence
RETURN: int
POINTS: 10

"""

import unittest
from Task101 import uniq_elements

class Task101Test(unittest.TestCase):
    """Testy do zadania 101"""

    def test_string(self):
        """Test na napisie."""
        self.assertEqual(uniq_elements("abracadabra"), 5)

    def test_number_list(self):
        """Test na liście liczb."""
        self.assertEqual(uniq_elements([1, 1, 2, 1, 10, 20, 2]), 4)

    def test_tuple(self):
        """Test na krotce."""
        self.assertEqual(uniq_elements((1, 2, 3, 1)), 3)

    def test_empty(self):
        """Test na pustej liście."""
        self.assertEqual(uniq_elements([]), 0)

if __name__ == '__main__':
    unittest.main()
