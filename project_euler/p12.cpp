/* Problem 10
   Highly divisible triangular number
*/

#include<iostream>

using namespace std;

int generator(int n)  // Generates nth triangular number 
{
	int num;
	num = 0;
	for(int i=1;i<=n;i++)
		num+=i;	
	
	return num;

}

int divisor(int num)	// Returns the number of divisors of number 'num'
{
	int count = 0;
	for(int i=1; i<=num; i++)
	{
		if(num%i == 0)
			count++;	

	}

	return count;
}

int triangle(int div) // Generates triangular number with over 'div' number of divisors
{
	int j,k;
	for(int i=1;;i++)
	{
		j = generator(i);
		k = divisor(j);
		cout << j << " Divisors: "<< k << endl;
		if(k>=div)
			return j;
	}
}


int main()
{
	int div;
	cout << "Enter upper limit on no. of divisors\n";
	cin >> div;	
	cout<<triangle(div)<<endl;
	
	return 0;
}
   
