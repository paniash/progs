#include<iostream>

using namespace std;

int main()
{
	int a,b,sum,max;
	a = 1;
	b = 2;
	sum = a;
	// Asks user to mention upper limit of sequence
	cout<<"What is the upper limit?"<<endl;
	cin>>max;
	while( (a<=max) || (b<=max))
	{
		int temp;
		temp = a;
		a = b;
		b = b + temp;

		if((a<=max) && (a%2==0))
			sum = sum+a;

	}
	cout<<sum-1<<endl;

	return 0;
	

}
