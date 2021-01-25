#include <stdio.h>

void selection_sort(int *arr, int N);
void show_array(int *arr, int N);

int main(void)
{
    int N = 7;
    int test1[] = {0, 5, -11, 555, 151, -500, 15555};
    selection_sort(test1, N);
    show_array(test1, N);
}

void selection_sort(int *arr, int N)
{
    for (int i = 0; i < N; i++)
    {
        int min = i;
        for (int j = i + 1; j < N; j++)
        {
            if (arr[j] < arr[min])
            {
                min = j;
            }
        }
        int temp = arr[min];
        arr[min] = arr[i];
        arr[i] = temp;
    }
}

void show_array(int *arr, int N)
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