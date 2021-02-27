#include <stdio.h>

/*
Problem:
Reverse a positive integer. 
Can you do it without using an additional data structure (arr, string, ect..)?
ex) 1234 -> 4321
*/

int reverse_int(int number)
{
    int res = 0;
    while (number > 0)
    {
        int rem = number % 10;
        number /= 10;
        res = res * 10 + rem;
    }
    return res;
}

int main(void)
{
    printf("%i\n", reverse_int(1234));
    printf("%i\n", reverse_int(1000054));
}