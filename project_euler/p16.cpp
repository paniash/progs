// Power digit sum
#include<iostream>

using namespace std;

int power(int n) // returns the product of 2 raised to the nth power
{
	int pr = 1;
	for(int i=1;i<=n;i++)
		pr*=i;

	return pr;
}


