#!/bin/sh

if [ $1 ]; then
    if [ "$1" = "run" ]; then
	echo "Uruchamianie lematyzatora:"
	if [ -f "lematyzator.app" ]; then
	    ./lematyzator.app
	else
	    echo "Zbuduj lematyzator!"
	fi
    elif [ -f data/$1 ]; then
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
	g++ -std=c++11 load_into_memory.cpp -o load_into_memory.app
	./load_into_memor.app
	g++ -O3 -std=c++11 lematyzator.cpp -o lematyzator.app
	echo "Lematyzator zbudowany"
	rm data/data*
	rm data/OpenFST*
	rm symbols.txt
    else
	echo "Pobierz PoliMorf i wypakuj!\nPlik powinien znajdzować się w folderze data pod nazwa PoliMorfX.tab - gdzie X oznacza wersje pliku!"
    fi
else
    echo "Nie podano argument!"
    echo "Przykładowe uruchomienie:"
    echo "\t./run.sh PoliMorf-0.6.7.tab\t - zbudowanie lematyzatora"
    echo "\t./run.sh run\t\t\t - uruchomienie lematyzatora"
fi

FST_PIPE () {
    fstcompile --isymbols=data/symbols.txt --osymbols=data/symbols.txt data/OpenFST_raw.txt | fstdeterminize | fstminimize | fstprint --isymbols=symbols.txt --osymbols=symbols.txt > data/OpenFST_out_text.fst
}
