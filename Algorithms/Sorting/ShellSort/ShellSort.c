#include <stdio.h>
#include <stdlib.h>

/* Prototypes */
void shell_sort(int *arr, int N);
void swap(int *arr, int i, int j);
void show_items(int *arr, int N);

int main(void)
{
    int N = 20;
    int *test1 = malloc(sizeof(int) * N);
    int *test2 = malloc(sizeof(int) * N);
    for (int i = 0; i < N; i++)
    {
        int rand1 = rand() * .000001;
        int rand2 = rand() * .000001;
        test1[i] = rand1;
        test2[i] = rand2;
    }
    printf("Arrays before sort:\n");
    show_items(test1, N);
    show_items(test2, N);
    shell_sort(test1, N);
    shell_sort(test2, N);
    printf("Arrays after sort:\n");
    show_items(test1, N);
    show_items(test2, N);
    free(test1);
    free(test2);
}

void shell_sort(int *arr, int N)
{
    // First find the start of the increment sequence 3x + 1
    int H = 1;
    while (H < N / 3)
    {
        H = 3 * H + 1;
    }
    while (H >= 1)
    {
        // Now we do insertion sort based on the decrement sequence of j -= H
        for (int i = H; i < N; i++)
        {
            for (int j = i; j >= H; j -= H)
            {
                if (arr[j] < arr[j - H])
                {
                    swap(arr, j, j - H);
                }
                else { break; }
            }
        }
        // decrement H
        H = H / 3;
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