#!/bin/bash

# Zadanie 203

# Napisz program Task203.py, który wyszuka wszystkie linie w tekście
# zawierające dane słowo i wypisze je sformatowane (szukane słowo w
# każdej linii jedno pod drugim oddzielone dwiema spacjami z lewej i
# prawej strony) razem z kontekstem przed i po wyniku wyszukiwania o
# długości n znaków. Szukane słowo oraz wartość n powinny być podawane
# jako argument programu (n domyślnie 15).

# head -250 grimms.txt | python Task203.py have 10

# Wyjście:

# me, I must  have  the whole
#  he was to  have  the golden
#  live, and  have  the
#  you would  have  carried aw

# POINTS: 10

. ../tests.sh

tested() {
    cat | python2 Task203.py of 6
}

run_test 203
exit $RESULT
