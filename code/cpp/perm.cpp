#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

std::vector<int> permute(std::vector<int> v) {
	std::vector<int> chg;

	int k = 1;
	do {
		std::vector<int> perm;
		for (auto e : v) {
			perm.push_back(e);
		}

		/*
		for (size_t i=0; i<perm.size(); i++)
			std::cout << perm[i];
		std::cout << "\n";
		*/
		if (k == 1)
			chg = perm;
		++k;
	}
	while (std::next_permutation(v.begin(), v.end()));

	return chg;
}

int main() {
	std::vector<int> v = {1,2,3,4};
	std::vector<int> chg;

	do {
		std::vector<int> perm;
		int k = 1;
		for (auto e : v) {
			perm.push_back(e);
		}

		for (size_t i=0; i<perm.size(); i++)
			std::cout << perm[i];
		std::cout << "\n";
		chg = perm;
	}
	while (std::next_permutation(v.begin(), v.end()));

	std::cout << "\nChanged vector: \n";
	for (size_t i = 0; i < v.size(); i++)
		std::cout << chg[i];
	std::cout << "\n";


	return 0;
}
