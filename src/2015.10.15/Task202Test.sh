#!/bin/bash

# Zadanie 202

# Napisz program Task202.py do generowania wszystkich n-gramów słów z
# podanego na standardowym wejściu stokenizowanego tekstu. N-gramem
# nazywamy ciąg występujących po sobie słów długości n. Program
# powinien wypisywać jeden n-gram w jendej linii wyjścia. Wartość n
# powinna być przyjmowana jako argument programu (domyślnie 3).
# cat grimms.txt | python2 Task202.py 3

# POINTS: 10

. ../tests.sh

tested() {
    cat | python2 Task202.py 5
}

run_test 202
exit $RESULT
