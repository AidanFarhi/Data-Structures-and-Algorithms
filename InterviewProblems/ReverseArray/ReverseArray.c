#include <stdio.h>

/*
Problem:
Reverse an array in place using no extra memory in O(N) time
*/

/* Function Prototypes */
void reverse_array(int *arr, int length);
void swap(int *arr, int i, int j);
void show_items(int *arr, int length);

int main(void)
{
    int test1[] = {1, 2, 3, 4, 5, 6, 7, 8, 9}; // odd # of items
    int test2[] = {1, 2, 3, 4, 5, 6, 7, 8};    // even # of items
    reverse_array(test1, 9);
    reverse_array(test2, 8);
    show_items(test1, 9);
    show_items(test2, 8);
}

void reverse_array(int *arr, int length)
{
    int i = 0;
    int j = length - 1;
    while (i < j)
    {
        swap(arr, i, j);
        ++i;
        --j;
    }
}

void swap(int *arr, int i, int j)
{
    int t = arr[i];
    arr[i] = arr[j];
    arr[j] = t;
}

void show_items(int *arr, int length)
{
    printf("[");
    for (int i = 0; i < length; i++)
    {
        if (i == length - 1) { printf("%i]\n", arr[i]); break; }
        printf("%i, ", arr[i]);
    }
}