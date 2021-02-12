#include <stdio.h>

/* Function Prototypes */
void heap_sort(int *arr, int N);
void heapify(int *arr, int N);
void sink(int *arr, int k, int N);
void swap(int *arr, int i, int j);
void show_items(int *arr, int N);

int main(void)
{
    int test[] = 
    {
        5, 1, -66, 141, 667, 73, 900, -611, 6616, 17, 
        -711, -567, 1, 777, 2, 1, -88, 2, 6, 7, 7, -222, 7, 22
    };
    heap_sort(test, 23);
    show_items(test, 23);
}

void heap_sort(int *arr, int N)
{
    heapify(arr, N);
    while (N > 0)
    {
        swap(arr, 0, N);
        sink(arr, 0, --N);
    }
}

void heapify(int *arr, int N)
{
    for (int i = N/2; i >= 0; i--)
    {
        sink(arr, i, N);
    }
}

void sink(int *arr, int k, int N)
{
    while (2*k <= N)
    {
        int j = 2*k;  // left child
        if (j < N && arr[j] < arr[j + 1]) { j++; } // find larger child
        if (arr[k] < arr[j]) 
        {
            swap(arr, k, j);
            k = j;
        }
        else { break; }
    }
}

void swap(int *arr, int i, int j)
{
    int t = arr[i];
    arr[i] = arr[j];
    arr[j] = t;
}

void show_items(int *arr, int N)
{
    printf("[");
    for (int i = 0; i <= N; i++)
    {
        if (i == N) { printf("%i]\n", arr[i]); break; }
        printf("%i, ", arr[i]);
    }
}