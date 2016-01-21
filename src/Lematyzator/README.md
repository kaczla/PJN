###Lematyzator
</br>

1) Pobrać <b>[PoliMorf](http://zil.ipipan.waw.pl/PoliMorf)</b>

2) Wypakować <b>PoliMorf</b> do folderu <b>data</b>

3) Urychomić skrypt: `./run.sh file` (gdzie <b>file</b> oznacza nazwę pliku PoliMorf)

</br>
</br>
Wymagania:
* Python 2.7
* g++
* [OpenFST](http://openfst.org/)

</br>
</br>
Uwagi:
* Czas budowy lematyzatora to ~30 minut lub więcej dla starszych maszyn
* Do determinizacji wymagane jest minimum 8GB RAM + 2GB SWAP lub 8GB+ RAM
* Ze słownika PoliMorf zostały usunięte wyrazy rozpoczynające się od "nie" oraz "naj", możlwe jest dodanie ich, ale należy edytować plik [convert_data.py](convert_data.py) i przeprowadzić cały proces ponownie
