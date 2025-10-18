#include <iostream>
#include <unordered_map>
using namespace std;

int main(){
    string text = "";
    string decyphered = "";

    unordered_map<char, char> rotalpha = {
        {'A', 'N'}, {'B', 'O'}, {'C', 'P'}, {'D', 'Q'},
        {'E', 'R'}, {'F', 'S'}, {'G', 'T'}, {'H', 'U'},
        {'I', 'V'}, {'J', 'W'}, {'K', 'X'}, {'L', 'Y'},
        {'M', 'Z'}, {'N', 'A'}, {'O', 'B'}, {'P', 'C'},
        {'Q', 'D'}, {'R', 'E'}, {'S', 'F'}, {'T', 'G'},
        {'U', 'H'}, {'V', 'I'}, {'W', 'J'}, {'X', 'K'},
        {'Y', 'L'}, {'Z', 'M'}, {'a', 'n'}, {'b', 'o'},
        {'c', 'p'}, {'d', 'q'}, {'e', 'r'}, {'f', 's'},
        {'g', 't'}, {'h', 'u'}, {'i', 'v'}, {'j', 'w'},
        {'k', 'x'}, {'l', 'y'}, {'m', 'z'}, {'n', 'a'},
        {'o', 'b'}, {'p', 'c'}, {'q', 'd'}, {'r', 'e'},
        {'s', 'f'}, {'t', 'g'}, {'u', 'h'}, {'v', 'i'},
        {'w', 'j'}, {'x', 'k'}, {'y', 'l'}, {'z', 'm'}
    };

    // Get input to decypher
    cout << "Enter text to decypher\n";
    cin >> text;

    // Loop thru text
    for(char i : text){
        //Char exist
        if(rotalpha.find(i) != rotalpha.end()){
            decyphered += rotalpha[i];
        }
        else {
            decyphered += i;
        }
    }

    cout << decyphered;
    return 0;
}
