#include <stdio.h>
#include <string.h>
/*
Problem:
Check if a string is a palindrome or not.
Ex) is_palindrome(level) -> True | is_palindrome(levels) -> False
*/

int is_palindrome(char *str) 
{
    int i = 0;
    int j = strlen(str) - 1;
    while (i <= j)
    {
        if (str[i] != str[j]) { return 1; }
        ++i;
        --j;
    }
    return 0;
}

int main(void)
{
    char *test1 = "level";
    char *test2 = "levels";
    if (is_palindrome(test1) == 0){ printf("%s: true\n", test1); } 
    else { printf("%s: false\n", test1); }
    if (is_palindrome(test2) == 0){ printf("%s: true\n", test2); } 
    else { printf("%s: false\n", test2); }
}