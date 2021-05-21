#include <stdio.h>
#include <math.h>

double compound_interest(double amount, double rate, double years) {
	double new_amount = 0.0;
	new_amount = amount * pow(1+rate, years);

	return new_amount;
}


int main() {
	double new_amount;
	new_amount = compound_interest(1000, 0.07, 25);
	printf("%f", new_amount);

	return 0;
}
