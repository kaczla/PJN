#!/bin/bash

# Zadanie 200

# Napisać program, który wypisuje liczbę znaków w każdym wierszu
# Zadanie jest już zrobione!!! To tylko przykład.

# POINTS: 0

. ../tests.sh

tested() {
    cat | python2 Task200.py
}

run_test 200
exit $RESULT
