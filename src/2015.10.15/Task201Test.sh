#!/bin/bash

# Zadanie 201


# Papisz program freq_words.py który zlicza liczbę wystąpień słów w
# tekście. Program powinien czytać dowolny tekst ze standardowego
# wejścia i wypisywać na standardowym wyjściu listę składającą się z par
# 'liczba wystąpień' i 'słowo' oddzielone znakiem tabulacji. Lista
# wynikowa powinna być posortowana po liczbie wystąpień. Słowa należy
# normalizować względem wielkości liter. Które 10 słów najczęściej
# występuje w Baśniach Braci Grimm?
# cat grimms.txt | python Task201.py | head

# POINTS: 10

. ../tests.sh

tested() {
    cat | python2 Task201.py
}

run_test 201
exit $RESULT
