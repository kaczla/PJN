#!/bin/bash

# Zadanie 205

# Napisz program Task205.py, który wypisze wszystkie takie zbiory wyrazów (jedna linia to jeden zbiór, wyrazy oddzielone spacją, kolejność nieistotna), w których wyrazy po usunięciu znaków diakrytycznych reprezentują to samo słowo (np. bąka, baka, baką). Program powinien czytać ze standardowego wejścia i pisać na standardowe wyjście. Przydatny może okazać się zestaw polskich liter diakrytyzowanych: 'ąćęłńóśźżĄĆĘŁŃÓŚŹŻ'.

# cat pantadeusz.txt | python diac_sets.py

# POINTS: 20

. ../tests.sh

tested() {
    cat | python2 Task205.py
}

run_test 205
exit $RESULT
