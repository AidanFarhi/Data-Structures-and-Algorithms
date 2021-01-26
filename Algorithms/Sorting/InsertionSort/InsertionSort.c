#include <stdio.h>
#include <stdlib.h>

/* Prototypes */
void insertion_sort(int *arr, int N);
void swap(int *arr, int i, int j);
void show_items(int *arr, int N);

int main(void)
{
    int N = 10;
    int *test1 = malloc(sizeof(int) * 10);
    int *test2 = malloc(sizeof(int) * 10);
    for (int i = 0; i < N; i++)
    {
        int rand1 = rand() * .00001;
        int rand2 = rand() * .00001;
        test1[i] = rand1;
        test2[i] = rand2;
    }
    printf("Before Sorting:\n");
    show_items(test1, N);
    show_items(test2, N);
    insertion_sort(test1, N);
    insertion_sort(test2, N);
    printf("After Sorting:\n");
    show_items(test1, N);
    show_items(test2, N);
    free(test1);
    free(test2);
}

void insertion_sort(int *arr, int N)
{
    for (int i = 0; i < N; i++)
    {
        for (int j = i; j > 0; j--)
        {
            if (arr[j] < arr[j - 1])
            {
                swap(arr, j, j - 1);
            }
            else { break; }
        }
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