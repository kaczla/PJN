#!/bin/sh

if [ $1 ]; then
    if [ -f data/$1 ]; then
	echo "Przetwarzanie PoliMorf (plik: $1)"
	./convert_data.py < data/$1
	echo "Pobieranie mapy znaków"
	./get_all_symbols.py < data/data_raw_out
	echo "Przetwarzanie do postaci OpenFST"
	./convert_to_OpenFST.py < data/data_raw_out
	echo "Przetwarzanie do postaci binarnej OpenFST"
	fstcompile --isymbols=data/symbols.txt --osymbols=data/symbols.txt data/OpenFST_raw.txt data/OpenFST_raw_binary.fst
	echo "Determinizowanie OpenFST"
	fstdeterminize data/OpenFST_raw_binary.fst data/OpenFST_det_binary.fst
	echo "Minimalizowanie OpenFST"
	fstminimize data/OpenFST_det_binary.fst data/OpenFST_min_binary.fst
	echo "Przetwarzanie do postaci tekstowej OpenFST"
	fstprint --isymbols=data/symbols.txt --osymbols=data/symbols.txt data/OpenFST_min_binary.fst data/OpenFST_out_text.fst
	echo "Przetwarzanie do postaci binarnej dla Lematyzatora"
	g++ -std=c++11 load_into_memory.cpp -o load_into_memory
	./load_into_memor
	g++ -std=c++11 lematyzator.cpp -o lematyzator
	echo "Lematyzator zbudowany"
	rm data/data*
	rm data/OpenFST*
	rm symbols.txt
    else
	echo "Pobierz PoliMorf i wypakuj!\nPlik powinien znajdzować się w folderze data pod nazwa PoliMorfX.tab - gdzie X oznacza wersje pliku!"
    fi
else
    echo "Nie podano nazwę pliku jako argument!\nPrzykładowe uruchomienie:\n\t./run.sh PoliMorf-0.6.7.tab"
fi

ALL () {
    fstcompile --isymbols=symbols.txt --osymbols=symbols.txt text.fst | fstdeterminize | fstminimize | fstprint --isymbols=symbols.txt --osymbols=symbols.txt
}
