#!/usr/bin/python2
# -*- coding: utf-8 -*-

"""
Zadanie 102

Napisz funkcję freq_dic(sequence), która zlicza liczbę wystąpień
elementów dla dowolnego typu sekwencyjnego. Funkcja powinna zwracać
słownik, w którym klucze odpowiadają elementom, a wartości liczbie
elementów. Dla łańcucha "abracadabra" wynikiem jest:

{"a":5, "b":2, "c":1, "d":1, "r":2}

NAME: freq_dic
PARAMS: sequence
RETURN: dictionary
POINTS: 10

"""

import unittest
from Task102 import freq_dic

class Task102Test(unittest.TestCase):
    """Testy do zadania 102"""

    def test_string(self):
        """Test na napisie."""
        self.assertEqual(freq_dic("abracadabra"), {"a": 5, "b": 2, "c": 1, "d": 1, "r": 2})

    def test_number_list(self):
        """Test na liście liczb."""
        self.assertEqual(freq_dic([1, 1, 2, 1, 10, 20, 2]), {1: 3, 2: 2, 10: 1, 20: 1})

    def test_tuple(self):
        """Test na krotce."""
        self.assertEqual(freq_dic((1, 2, 3, 1)), {1: 2, 2: 1, 3: 1})

    def test_empty(self):
        """Test na pustej liście."""
        self.assertEqual(freq_dic([]), { })

if __name__ == '__main__':
    unittest.main()
