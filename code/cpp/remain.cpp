#include <iostream>
#include <string>
#include <sstream>
using namespace std;

int main() {
    string str = "Rz(q[0], -1.000000*gamma1);\nCX(q[0],q[1]);\nRz(q[1], 2.000000*gamma1);\nCX(q[0],q[1]);\nH(q[0]);\nRz(q[0], 2.000000*beta1);\nH(q[0]);\n H(q[1]);\nRz(q[1], 2.000000*beta1);\n";

    const string a[4] = {"101", "202", "303", "404"};

    int count = 0;
    int pos = str.find('*');
    while (pos < str.length()+1) {
        const int pos_brace = str.find(')', pos + 1);
        const int length = pos_brace - pos - 1;
        str.replace(pos+1, length, a[count++]);
        pos = str.find('*', pos+1);
    }

    cout << str << endl;

    return 0;
}
