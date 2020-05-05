// Finding the sum of primes below a given number n
#include<iostream>

using namespace std;

int main()
{
	long int n, sum;
	sum = 0;
	cout <<"Enter the upper prime\n";
	cin >> n;
	for(long int i=1; i<n; i++)
	{
		int ct = 0;
		for(long int j=1; j<=i; j++)
		{
			if(i%j == 0)
				ct++;
		}

		if(ct == 2)
		{
			cout<<i<<endl;
			sum+=i;

		}
	}

	cout<<"Sum: "<<sum<<endl;

	return 0;

}
