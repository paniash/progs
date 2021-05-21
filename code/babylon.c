#include <stdio.h>
#include <math.h>
#include <stdlib.h>

double babylonian_sqrt(double S) {
	double next_guess, init_guess = 20;
	double xn = init_guess;

	double err = pow(10, -10);
	while ((abs(xn*xn - S) / S) > err) {
		next_guess = 1/2 * (xn + S/xn);
		xn = next_guess;
	}

	return xn;
}

int main() {
	double sq, S = 2;
	sq = babylonian_sqrt(S);
	printf("%f", sq);
	return 0;

}
