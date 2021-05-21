#include <iostream>
#include <vector>
#include <algorithm>

std::vector<double> permute(std::vector<double> v, int j) {
	std::vector<double> chg;

	int k = 1;
	do {
		std::vector<double> perm;
		for (auto e : v) {
			perm.push_back(e);
		}

		/*
		for (size_t i=0; i<perm.size(); i++)
			std::cout << perm[i];
		std::cout << "\n";
		*/
		if (k == j)
			chg = perm;
		++k;
	}
	while (std::next_permutation(v.begin(), v.end()));

	return chg;
}


int main() {
	std::vector<double> v = {1.012, 2.294, 3.356, 4.847};
	std::vector<double> chg;

	chg = permute(v, 1);

	std::cout << "\nChanged vector: \n";
	for (size_t i = 0; i < chg.size(); i++)
		std::cout << chg[i] << " ";
	std::cout << "\n";

	return 0;
}
