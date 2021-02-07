#include <stdio.h>

/* Prototypes */
void quick_sort(int *arr, int N);
void quick_sort_helper(int *arr, int lo, int hi);
int partition(int *arr, int lo, int hi);
void swap(int *arr, int x, int y);
void show_items(int *arr, int N);

int main(void)
{
    int test[] = {5, 1, -66, 141, 667, 73, 900, -611, 6616, 17, -711, -567, 1, 777, 2, 1, -88, 2, 6, 7, 7, -222, 7, 22};
    quick_sort(test, 24);
    show_items(test, 24);
}

void quick_sort(int *arr, int N)
{
    quick_sort_helper(arr, 0, N - 1);
}

void quick_sort_helper(int *arr, int lo, int hi)
{
    if (hi <= lo) { return; }
    int p = partition(arr, lo, hi);
    quick_sort_helper(arr, lo, p - 1);
    quick_sort_helper(arr, p + 1, hi);
}

int partition(int *arr, int lo, int hi)
{
    int i = lo;
    int j = hi + 1;
    while (1)
    {
        while (arr[lo] > arr[++i])
        {
            if (i == hi) { break; }
        }
        while (arr[lo] < arr[--j])
        {
            if (j == lo) { break; }
        }
        if (i >= j) { break; }
        swap(arr, i, j);
    }
    swap(arr, lo, j);
    return j;
}

void swap(int *arr, int x, int y)
{
    int temp = arr[x];
    arr[x] = arr[y];
    arr[y] = temp;
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