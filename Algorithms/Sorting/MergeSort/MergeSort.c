#include <stdio.h>

/* Prototypes */
void merge(int *arr, int *aux, int lo, int mid, int hi);
void sort(int *arr, int N);
void sort_helper(int *arr, int *aux, int lo, int hi);
void show_items(int *arr, int N);

int main(void)
{
    int test[18] = {6, 1, 7, 3, 4, 11, -66, 141, 664, -26, 1616, 2, 88, 1, 755, -2, -66, -2777};
    int N = 18;
    sort(test, N);
    show_items(test, N);
}

void sort(int *arr, int N)
{
    int aux[N];
    sort_helper(arr, aux, 0, N - 1);
}

void sort_helper(int *arr, int *aux, int lo, int hi)
{
    if (hi <= lo) { return; }
    int mid = lo + (hi - lo) / 2;
    sort_helper(arr, aux, lo, mid);
    sort_helper(arr, aux, mid + 1, hi);
    merge(arr, aux, lo, mid, hi);
}

void merge(int *arr, int *aux, int lo, int mid, int hi)
{
    // Copy arr into aux array
    for (int n = lo; n <= hi; n++) { aux[n] = arr[n]; }
    // Merge two halves
    int l = lo, r = mid + 1;
    for (int k = lo; k <= hi; k++)
    {
        if (l > mid) { arr[k] = aux[r++]; }
        else if (r > hi) { arr[k] = aux[l++]; }
        else if (aux[l] < aux[r]) { arr[k] = aux[l++]; }
        else { arr[k] = aux[r++]; }
    }
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
