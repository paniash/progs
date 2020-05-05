// Prime number generator
// Generates prime numbers upto a limit (specified by the user) and also outputs the number of such primes
#include<iostream>

using namespace std;

// function to check if a number is prime
int prime(long int num)
{
	int count = 0;
	for(long int l=1; l<=num; l++)
	{
		if(num%l == 0)
			count++;

	}

	if(count==2)
		return 1;

	return 0;
}
	

int main()
{
	long int max;
	long int ct=0;
	cout<<"Enter an upper limit:\n";
	cin>>max;
	cout<<"Prime numbers upto "<<max<<":"<<endl;
	for(long int i=2;i<max;i++)
	{
		if(prime(i) == 1)
		{
			cout<<i<<endl; // outputs the prime numbers
			ct++;
		}

	}

	cout<<"Total number of primes: "<<ct<<endl;

	return 0;

}
