#include <iostream>
#include <string>
#include <sstream>
using namespace std;

int main() {
    stringstream os;
    string str("Hello there.\nGeneral Kenobi!");
    os << str;
    string line;
    while (!os.eof()) {
        string temp;
        os >> temp;
        cout << temp << endl;
    }

    return 0;
}
