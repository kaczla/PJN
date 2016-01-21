#include <iostream>
#include <cstdlib>
#include <string>
#include <fstream>
#include <sstream>
#include <map>
#include <locale>
#include <vector>
#include <set>
#include <algorithm>
#include <sys/resource.h>

using namespace std;

int main(int argc, char* argv[]){
  locale::global(locale(""));
  const rlim_t kStackSize = 128 * 1024 * 1024;
  map <wchar_t, int> KeyMap;
  map <int, wchar_t> KeyMapReversed;
  int StatesSizeX, StatesSizeY, StatesFinalSizeX;
  set <int> FinalState;
  vector <wstring> toAdd;
  vector <wstring>::iterator toAddIt;
  map <wchar_t, int> removeChar {
    { L'0', 0 }, { L'A', 1 }, { L'B', 2 }, { L'C', 3 }, { L'D', 4 },
    { L'E', 5 }, { L'F', 6 }, { L'G', 7 }, { L'H', 8 }, { L'I', 9 },
    { L'J', 10 }, { L'K', 11 }, { L'L', 12 }, { L'M', 13 }, { L'N', 14 },
    { L'O', 15 }, { L'P', 16 }, { L'R', 17 }, { L'S', 18 }, { L'T', 19 },
    { L'U', 20 }, { L'W', 21 }, { L'X', 22 }, { L'Y', 23 }, { L'Z', 24 },
    { L'a', 25 }, { L'b', 26 }, { L'c', 27 }, { L'd', 28 }, { L'e', 29 },
    { L'f', 30 }, { L'g', 31 }, { L'h', 32 }, { L'i', 33 }, { L'j', 34 },
    { L'k', 35 }, { L'l', 36 }, { L'm', 37 }, { L'n', 38 }, { L'o', 39 },
    { L'p', 40 }, { L'r', 41 }, { L's', 42 }, { L't', 43 }, { L'u', 44 },
    { L'w', 45 }, { L'x', 46 }, { L'y', 47 }, { L'z', 48 }
  };
  int i,j;
  {
    wstring tmp_string;
    wifstream file;
    file.open("data/lematyzator_map", ios::in);
    if(file.good()){
      //SIZE
      file>>tmp_string;
      if(tmp_string != L"SIZE"){
        wcout<<L"ERROR (SIZE): Problem z plikiem data/lematyzator_map!\n";
        return 0;
      }
      else{
        file>>StatesSizeX>>StatesSizeY>>StatesFinalSizeX;
      }
      //KEY MAP
      file>>tmp_string;
      if(tmp_string != L"KEY"){
        wcout<<L"ERROR (KEY): Problem z plikiem data/lematyzator_map!\n";
        return 0;
      }
      else{
        wchar_t input_char;
        int input_number;
        for(int i=0; i<StatesSizeY; ++i){
          file>>input_char;
          file>>input_number;
          KeyMap[input_char] = input_number;
          KeyMapReversed[input_number] = input_char;
        }
      }
      //FINAL STATE
      file>>tmp_string;
      if(tmp_string != L"FINAL"){
        wcout<<L"ERROR (FINAL): Problem z plikiem data/lematyzator_map - błedna ilość znaków do pobrania!\n";
        return 0;
      }
      else{
        int input_number;
        for(int i=0; i<StatesFinalSizeX; ++i){
          file>>input_number;
          FinalState.insert(input_number);
        }
      }
    }
    else{
      wcout<<L"Problem z plikiem: data/lematyzator_map\n";
      return 0;
    }
    file.close();
  }
  //STACK SIZE
  {
    rlimit rl;
    int result = getrlimit(RLIMIT_STACK, &rl);
    rl.rlim_cur = kStackSize;
    result = setrlimit(RLIMIT_STACK, &rl);
  }
  int States[StatesSizeX][StatesSizeY];
  // int ** States = new int*[StatesSizeX];
  for(int i=0; i<StatesSizeX; ++i){
    // States[i] = new int[StatesSizeY];
    fill_n(States[i], StatesSizeY, -1);
  }
  {
    ifstream file;
    file.open("data/lematyzator_data", ios::in);
    if(file.good()){
      int begin_state, end_state, char_state;
      while(file>>begin_state>>end_state>>char_state){
        States[begin_state][char_state] = end_state;
      }
    }
    else{
      wcout<<L"Problem z plikiem: data/lematyzator_data\n";
      return 0;
    }
    file.close();
  }
  wstring input_word, output_word;
  wcout<<L"Wciśnij CTRL + D, aby zakończyć!\nPodaj słowo:\n";
  int start, next;
  while(wcin>>input_word){
    start = 0;
    next = 0;
    wcout<<L"Dla słowa: "<<input_word<<"\n";
    for(i=0; i<input_word.size(); ++i){
      if(KeyMap.find(input_word[i]) == KeyMap.end()){
          start = -1;
          break;
      }
      else{
        next = KeyMap[input_word[i]];
        start = States[start][next];
      }
      if(start < 0){
        break;
      }
    }
    toAdd.clear();
    if(start < 0){
      wcout<<L"\tBrak słowa w słowniku!\n";
    }
    else {
      next = KeyMap[L'+'];
      start = States[start][next];
      if(start < 0){
        wcout<<L"\tBrak słowa w słowniku!\n";
      }
      else{
        wstring t;
        int start2;
        for(i=0;i<StatesSizeY;++i){
          if(States[start][i] != -1){
            t.clear();
            start2 = States[start][i];
            t+=KeyMapReversed[i];
            while(FinalState.find(start2) == FinalState.end()){
              for(j=0;j<StatesSizeY;++j){
                if(States[start2][j] != -1){
                  start2 = States[start2][j];
                  t+=KeyMapReversed[j];
                  break;
                }
              }
              if(j==StatesSizeY){
                break;
              }
            }
            if(FinalState.find(start2) != FinalState.end()){
              toAdd.push_back(t);
            }
            else{
              wcout<<L"\tBrak słowa w słowniku!\n";
            }
          }
        }
      }
      for(toAddIt = toAdd.begin(); toAddIt != toAdd.end(); ++toAddIt){
        i = removeChar[(*toAddIt)[0]];
        output_word.assign(input_word.begin(), input_word.end()-i);
        output_word.append(toAddIt->begin()+1, toAddIt->end());
        wcout<<L"\t"<<output_word<<L"\n";
      }
      wcout<<L"\n";
      }
  }
  // for(i=0; i<StatesSizeX; ++i){
  //   delete [] States[i];
  // }
  // delete [] States;
  return 0;
}
