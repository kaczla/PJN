#include <iostream>
#include <cstdlib>
#include <string>
#include <fstream>
#include <sstream>
#include <map>
#include <locale>
#include <vector>
#include <algorithm>

using namespace std;

int main(int argc, char* argv[]){
  locale::global(locale(""));
  map <wchar_t,int> KeyMap;
  vector <int> FinalState;
  vector <int*> States;
  int counter_map = 0;
  wstringstream to_file;
  wfstream file_save, file_save_2;
  file_save.open("data/data.bin", ios::out | ios::binary);
  file_save_2.open("data/map.bin", ios::out | ios::binary);
  {
    wifstream file_map_char;
    file_map_char.open("data/symbols.txt",ios::in);
    wchar_t input_char;
    int input_number;
    if(file_map_char.good()){
      to_file<<"KEY\n";
      while(file_map_char>>input_char){
        file_map_char>>input_number;
        KeyMap[input_char] = counter_map;
        to_file<<input_char<<" "<<counter_map<<"\n";
        ++counter_map;
      }
      --counter_map;
    }
    else{
      cout<<"Problem z plikiem: data/symbols.txt\n";
      return 0;
    }
    if(counter_map < 0){
      cout<<"Problem z mapą znaków!\n";
      return 0;
    }
    file_map_char.close();
    wifstream file_input;
    file_input.open("data/OpenFST_out_text.fst", ios::in);
    wstring input_string;
    size_t begin_find = 0;
    size_t found = 0;
    int begin_state, end_state, char_state;
    if(file_input.good()){
      while(getline(file_input,input_string)){
        begin_find = 0;
        found = input_string.find(L"\t", begin_find);
        if(found == string::npos){
          FinalState.push_back(stoi(input_string));
        }
        else{
          begin_state = stoi(input_string.substr(begin_find,found-begin_find));
          begin_find = found+1;
          found = input_string.find(L"\t", begin_find);
          if(found != string::npos){
            end_state = stoi(input_string.substr(begin_find,found-begin_find));
            begin_find = found+1;
            found = input_string.find(L"\t", begin_find);
            if(found != string::npos){
              input_char = input_string.substr(begin_find,found-begin_find)[0];
              char_state = KeyMap[input_char];
              if(begin_state>end_state){
                if(begin_state >= States.size()){
                  for(int i=0; i<begin_state-States.size()+1; ++i){
                    States.push_back(new int[counter_map]);
                    fill_n(States.back(), counter_map, -1);
                  }
                }
              }
              else{
                if(end_state >= States.size()){
                  for(int i=0; i<end_state-States.size()+1; ++i){
                    States.push_back(new int[counter_map]);
                    fill_n(States.back(), counter_map, -1);
                  }
                }
              }
              try{
                file_save<<begin_state<<" "<<end_state<<" "<<char_state<<"\n";
                States[begin_state][char_state] = end_state;
              }
              catch(...){
                wcout<<"States["<<begin_state<<"]["<<char_state<<"] = "<<end_state<<"\n";
              }
            }
          }
        }
      }
    }
    else{
      cout<<"Problem z plikiem: data/OpenFST_out_text.fst\n";
      return 0;
    }
    file_input.close();
  }
  file_save.close();
  file_save_2<<"SIZE\n";
  file_save_2<<States.size()<<" "<<counter_map<<" "<<FinalState.size()<<"\n";
  file_save_2<<to_file.rdbuf();
  file_save_2.close();
  States.clear();
  return 0;
}
