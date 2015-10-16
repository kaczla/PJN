#!/usr/bin/python2
# -*- coding: utf-8 -*-

"""
Zadanie 106

Napisz program do zastępowania wyrazów (wyrazem nazywamy dowolny ciąg
znaków oddzielony białymi znakami) w tekście według słownika
zdefiniowanego w pliku, którego nazwa będzie podawana jako argument
programu. W słowniku w osobnych liniach znajdują się pary wyrazów
oddzielone znakiem tabulacji, które mówią jaki wyraz należy zamienić
na jaki, np.:

Ala   Alicja
ma    mieć
kota  kot

Dla powyższego słownika i tekstu "Ala ma kota i psa" wczytanego ze
standardowego wejścia program powinien wypisać na standardowe wyjście:
"Alicja mieć kot i psa".

Główna funkcja powinna nazywać się replace_words.

NAME: replace_words
PARAMS: string, string
RETURN: string
POINTS: 20

"""

import unittest
from Task106 import replace_words

class Task106Test(unittest.TestCase):
    """Testy do zadania 106"""

    def test_main(self):
        """Główny test."""
        self.assertEqual(replace_words("Ala ma kota i psa", "Task106Test.dat"),
                         "Alicja mieć kot i psa")

if __name__ == '__main__':
    unittest.main()
