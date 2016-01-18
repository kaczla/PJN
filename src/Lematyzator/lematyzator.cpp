#include <iostream>
#include <cstdlib>
#include <string>
#include <fstream>
#include <sstream>
#include <map>
#include <locale>
#include <vector>
#include <algorithm>
#include <sys/resource.h>

using namespace std;

int main(int argc, char* argv[]){
  locale::global(locale(""));
  const rlim_t kStackSize = 128 * 1024 * 1024;
  map <wchar_t, int> KeyMap;
  int StatesSizeX, StatesSizeY, StatesFinalSizeX;
  {
    wstring tmp_string;
    int size;
    wifstream file;
    file.open("data/map.bin", ios::in);
    if(file.good()){
      //SIZE
      file>>tmp_string;
      if(tmp_string != L"SIZE"){
        cout<<"ERROR (SIZE): Problem z plikiem data/map.bin!\n";
      }
      else{
        file>>StatesSizeX>>StatesSizeY>>StatesFinalSizeX;
      }
      //KEY MAP
      file>>tmp_string;
      if(tmp_string != L"KEY"){
        cout<<"ERROR (KEY): Problem z plikiem data/map.bin!\n";
      }
      else{
        wchar_t input_char;
        int input_number;
        for(int i=0; i<size; ++i){
          file>>input_char;
          file>>input_number;
          KeyMap[input_char] = input_number;
        }
      }
    }
    else{
      cout<<"Problem z plikiem: data/map.bin\n";
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
  for(int i=0; i<StatesSizeX; ++i){
    fill_n(States[i], StatesSizeY, -1);
  }
  {
    ifstream file;
    file.open("data/data.bin", ios::in);
    if(file.good()){
      int begin_state, end_state, char_state;
      while(file>>begin_state>>end_state>>char_state){
        States[begin_state][char_state] = end_state;
      }
    }
    else{
      cout<<"Problem z plikiem: data/data.bin\n";
    }
    file.close();
  }
  wstring input_word;
  cout<<"Wciśnij CTRL + D, aby zakończyć!\nPodaj słowo:\n";
  int i, start, next;
  while(wcin>>input_word){
    start = 0;
    next = 0;
    for(i=0; i<input_word.size(); ++i){
      if(KeyMap.find(input_word[i]) == KeyMap.end()){
          cout<<"Brak słowa w słowniku!\n";
          break;
      }
      next = KeyMap[input_word[i]];
      start = States[start][next];
      if(start < 0){
        cout<<"Brak słowa w słowniku!\n";
        break;
      }
    }
  }
  return 0;
}
