#include<iostream>

using namespace std;

int main()
{
	int max, sum;
	sum = 0;
	max = 1000;
	for(int i=1;i<max;i++)
	{
		if((i%3 == 0) || (i%5 == 0))
		{
			sum = sum + i;
		}

	}

	cout<<"The sum is "<<sum<<endl;
	return 0;

}
