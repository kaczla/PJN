#!/bin/sh

if [ $1 ]; then    
    if [ -f data/$1 ]; then
	echo "Przetwarzanie PoliMorf (plik: $1)"
	./convert_data.py < data/$1
	echo "Pobieranie mapy znaków"
	./get_all_symbols.py < data/data_raw_out
	echo "Przetwarzanie do postaci OpenFST"
	./convert_to_OpenFST.py < data/data_raw_out
	echo "Lematyzator zbudowany"
    else
	echo "Pobierz PoliMorf i wypakuj!\nPlik powinien znajdzować się w folderze data pod nazwa PoliMorfX.tab - gdzie X oznacza wersje pliku!"
    fi
else
    echo "Nie podano nazwę pliku jako argument!\nPrzykładowe uruchomienie:\n\t./run.sh PoliMorf-0.6.7.tab"
fi
