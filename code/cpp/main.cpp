#include <iostream>
#include <string>
#include <sstream>
#include <vector>
using namespace std;

string replacer(string str, const std::vector<double>& params) {
    size_t count = 0;
    size_t pos = str.find('*');
    // size_t pos1 = str.find('/', pos+1);
    while (pos != string::npos) {
        size_t pos_brace = str.find(')', pos + 1);
        size_t length = pos_brace - pos - 1;
        str.replace(pos+1, length, to_string(params[count++]));
        pos = str.find('*', pos+1);
    }

    return str;
}


int main() {
    string str = "Rz(q[0], -1.000000*gamma1);\nCX(q[0],q[1]);\nRz(q[1], 2.000000*gamma1);\nCX(q[0],q[1]);\nH(q[0]);\nRz(q[0], 2.000000*beta1);\nH(q[0]);\n H(q[1]);\nRz(q[1], 2.000000*beta1);\n";

    // string str = "H(q[0]);\nH(q[1]);\n Rz(q[0], -1.000000*gamma0);\n CX(q[0],q[1]);\nRz(q[1], 2.000000*gamma0);\nCX(q[0],q[1]);\nH(q[0]);\nRz(q[0], 2.000000*beta0);\nH(q[0]);\nH(q[1]);\n Rz(q[1], 2.000000*beta0);\nH(q[1]);\nRz(q[0], -1.000000*gamma1);\nCX(q[0],q[1]);\nRz(q[1], 2.000000*gamma1);\nCX(q[0],q[1]);\nH(q[0]);\nRz(q[0], 2.000000*beta1);\nH(q[0]);\nH(q[1]);\nRz(q[1], 2.000000*beta1);\nH(q[1]);\n";

    // string a[4] = {"101", "202", "303", "404"};
    vector<double> vec;
    vec.assign(4, 302);
    string new_str = replacer(str, vec);
    cout << new_str << endl;

    return 0;
}
