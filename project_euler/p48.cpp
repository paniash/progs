// Self powers
#include<iostream>

using namespace std;

int power(int num) //returns a number raised to itself
{
	int pr = num;
	long int sum = 1;
	for(int i=1; i<=num; i++)
		sum *= pr;	

	return sum;

}

int psum(int num) //adds power(n) where n is a natural number from n=1 to n=num
{
	long int sum=0;
	for(int i=1;i<=num;i++)
		sum+=power(i);

	return sum;
}

int main()
{
	int num;
	long int c;
	cout << "Enter a number\n";
	cin >> num;
	c = psum(num);
	cout << "Result: " << c << endl;
	return 0;
}
