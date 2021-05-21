#include <iostream>
#include <vector>
#include <string>
using namespace std;

int factorial(vector<int> vec) {
	int prod = 1;
	for (size_t i=1; i < vec.size(); i++) {
		prod *= i;
	}

	return prod;
}

int main() {
	vector<int> vec;

	for (int i = 0; i < 5; i ++) {
		vec.push_back(i);
	}

	const vector<int> sec = vec;

	cout << "Original vector elements: ";
	for (size_t i = 0; i < sec.size(); i++) {
		cout << sec[i] << " ";
	}

	size_t j = vec.size();
	double temp1 = vec[vec.size()-1];
	double temp2 = vec[vec.size()-2];
	while (j > 0) {
		vec[j] = vec[j-2];
		j--;
	}
	vec[1] = temp1;
	vec[0] = temp2;

	cout << "\nModified elements: ";
	for (size_t i = 0; i < vec.size(); i++) {
		cout << vec[i] << " ";
	}

	cout << "Factorial: " << factorial(vec) << "\n";

	return 0;
}
