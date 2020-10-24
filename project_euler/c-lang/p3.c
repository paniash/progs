// Largest prime factor of the number 6008511475143
#include <stdio.h>

// returns TRUE if number if prime
int prime(long int num)
{
    int count;
    count = 0;
    for(int i=1; i<=num; i++)
        if(num % i ==0)
            count++;

    if(count == 2)
        return 1;
    else
        return 0;
}

int main()
{
    int count;
    long int num;
    long int max;
    max = 0;
    num = 600851475143;
    for(int i=1; i<=num; i++)
        if(num % i == 0)
        {
            printf("i: %d\n", i);
            if(prime(i) == 1)
            {
                if(max < i)
                    max = i;
            }
        }
    printf("Max: %d\n", max);

    return 0;
}
