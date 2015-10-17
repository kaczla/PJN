#!/bin/bash

# Zadanie 204

# Napisz program Task204.py, który zlicza liczbę wystąpień liter w tekście podanym na standardowym wejściu i wypisuje je w postaci par 'litera' 'liczba wystąpień' oddzielone znakiem tabulacji. Należy zliczyć duże litery A-Z oraz małe litery a-z z alfabetu ASCII. Wyjście powinno być posortowane wg. liter w kolejności alfabetycznej.


# head -200 grimms.txt | python Task204.py

# Wyjście (wartości nie muszą się zgadzać z powyższym poleceniem):

# A       839
# B       383
# C       251
# ...

# POINTS: 10

. ../tests.sh

tested() {
    cat | python2 Task204.py
}

run_test 204
exit $RESULT
