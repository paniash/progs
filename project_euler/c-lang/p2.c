#include <stdio.h>

int main()
{
    int a, b, lim, sum;
    a = 1;
    b = 2;
    sum = 0;
    lim = 4000000;
    while(a <= lim)
    {
        printf("%d\n", a);
        int temp = 0;
        temp = b;
        b = a+b;
        a = temp;
        if(a%2 == 0)
            sum += a;
    }
    printf("Sum: %d", sum);

    return 0;
}
