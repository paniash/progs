// Finding the nth prime number
#include<iostream>

using namespace std;

int main()
{
	int n, ct, i;
	i = 2;
	ct = 0;
	//asks user for the value of n
	cout << "Enter the value of n"<<endl;
	cin >> n;
	while(ct != n)
	{
		int ct1 = 0;
		for(int j=1; j<=i; j++)
		{
			if(i%j == 0)
				ct1++;	
		
		}	

		if(ct1 == 2)
			ct++;	

		i++;

	}

	cout<<i-1<<endl;

	return 0;

}
