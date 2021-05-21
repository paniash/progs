#include <iostream>
#include <string>
#include <sstream>
using namespace std;

int main() {
    const string str("Rz(q[0], -1.000000*gamma1);\nCX(q[0],q[1]);\nRz(q[1], 2.000000*gamma1);\nCX(q[0],q[1]);\n H(q[0]);\nRz(q[0], 2.000000*beta1);\nH(q[0]);\n H(q[1]);\nRz(q[1], 2.000000*beta1);\n");

    stringstream os;
    os << str;
    string line;
    const char *a[4] = {"101", "202", "303", "404"};

    int count = 0;
    while (getline(os, line)) {
        for (const char byte : line) {
            if (byte == '*') {
                int length = line.substr(line.find('*')+1, line.find(')') - line.find('*')-1).length();
                line.replace(line.find('*')+1, length, a[count]);
                cout << line << endl;
                count++;
                // cout << line.substr(line.find('*')+1, line.find(')') - line.find('*')-1) << endl;
            }
        }
    }

    return 0;
}
