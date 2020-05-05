// Outputs the prime factors of a number 
#include<iostream>

using namespace std;

/*
// Function to find the largest number in an array
int large(int arr[], int size)
{
	large = arr[0];
	for(int i=0;i<size;i++)
	{
		if(arr[i] > large)
			large = arr[i];
	}

	return large;

}
*/

// Function to check if the given number is prime
int prime(long int num)
{
	int count = 0;
	for(long int l=1;l<=num;l++)
	{
		if(num%l == 0)
		{
			count++;
		}
	}

	if(count == 2)
		return 1;	
	
	return 0;

}


int main()
{
	long int num;
	// asks user for the input
	cout<<"Enter a number:\n";
	cin>>num;
	cout<<"Prime factors:\n";
	for(long int i=1; i<num; i++)	
	{
		if(num%i == 0)
		{
			if(prime(i) == 1)
				cout<<i<<endl;
		}
	}


	return 0;


}
