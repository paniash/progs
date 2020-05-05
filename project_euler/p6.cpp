// Sum square difference
#include<iostream>

using namespace std;

int sum_square(int n)  // finds the sum of squares of first n natural numbers
{
	int sum=0;
	for(int i=1;i<=n;i++)
		sum+=i*i;
	
	
	return sum;
}

int square_sum(int n) // finds the square of sum of first n natural numbers
{
	
	int sum=0;
	for(int i=1;i<=n;i++)
		sum+=i;
	
	
	return sum*sum;
}



int main()
{
	int diff, num;
	cout << "Enter the upper limit of natural numbers\n";
	cin >> num;
	diff = square_sum(num) - sum_square(num);
	cout << "Result: " << diff << endl;
	
	return 0;	
}

