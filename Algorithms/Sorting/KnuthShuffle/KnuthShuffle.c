#include <stdio.h>
#include <stdlib.h>

/* Prototypes */
void knuth_shuffle(int *arr, int N);
void swap(int *arr, int i, int j);
void show_items(int *arr, int N);

int main(void)
{
    int N = 9;
    int test[] = {1, 2, 3, 4, 5, 6, 7, 8, 9};
    knuth_shuffle(test, N);
    show_items(test, N);
}

void knuth_shuffle(int *arr, int N)
{
    for (int i = 0; i < N; i++)
    {
        int r = rand() % (N - i) + i;
        swap(arr, i, r);
    }
}

void swap(int *arr, int i, int j)
{
    int temp = arr[i];
    arr[i] = arr[j];
    arr[j] = temp;
}

void show_items(int *arr, int N)
{
    printf("[");
    for (int i = 0; i < N; i++)
    {
        if (i == N - 1)
        {
            printf("%i]\n", arr[i]);
            break;
        }
        printf("%i, ", arr[i]);
    }
}