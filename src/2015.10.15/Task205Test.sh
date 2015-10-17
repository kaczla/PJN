#!/bin/bash

# Zadanie 205



# POINTS: 20

. ../tests.sh

tested() {
    cat | python2 Task205.py
}

run_test 205
exit $RESULT
