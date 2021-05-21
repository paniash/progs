#include <iostream>
#include <string>
#include <sstream>
using namespace std;

int main() {
    string str = "This is a line.\n(1*temp1);\n(2*temp2);\n(3*temp3);\nEnd of string.\n";
    const string a[3] = {"101", "202", "303"};

    size_t counter = 0;
    size_t pos = str.find('*');
    while (pos != string::npos) {
        str.replace(pos+1, 5, a[counter++]);
        pos = str.find('*', pos+1);
    }

    cout << str << "\n";

    return 0;
}
