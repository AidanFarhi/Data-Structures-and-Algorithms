#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

/* Function Prototypes */
int insert(int item);
int is_empty();
int get_max();
int del_max();
void sink(int i);
void swim(int i);
void swap(int i, int j);
void show_items(int *arr, int n);

/* Global Variables */
int *pq; 
int N; 
int capacity;

/* Test Client */
int main(int argc, char *argv[])
{
    if (argc != 2)
    {
        printf("Usage: ./MaxPQ <test file.txt>\n");
        return 1;
    }
    char test[1024];
    getcwd(test, 1024);
    strcat(test, "/Tests/");
    strcat(test, argv[1]);
    char buffer[255];
    FILE *file = fopen(test, "r");
    fgets(buffer, 255, file);
    int capacity = atoi(buffer);
    N = 0;
    pq = malloc(sizeof(int) * (capacity + 1));
    while (fgets(buffer, 255, file) != NULL)
    {
        insert(atoi(buffer));
    }
    int arr[capacity];
    for (int n = 0; n < capacity; n++)
    {
        arr[n] = del_max();
    }
    show_items(arr, capacity);
    free(pq);
    fclose(file);
    return 0;
}

/* Priority Queue Functions */
int insert(int item)
{
    if (N == capacity - 1)
    {
        printf("pq at max capacity: %i\n", capacity);
        return 1;
    }
    pq[++N] = item;
    swim(N);
    return 0;
}

int is_empty()
{
    if (N == 0) { return 0; }
    else { return 1; }
}

int get_max()
{
    return pq[1];
}

int del_max()
{
    int max = get_max();
    swap(1, N--);
    sink(1);
    return max;
}

void sink(int i)
{
    while (2*i <= N)
    {
        int j = 2*i; // left child
        if (j < N && pq[j] < pq[j + 1]) { j++; } // find out which child is greater
        if (pq[i] < pq[j])  // if parent less than child
        {
            swap(i, j);  // swap parent and child
            i = j; // sink down tree
        }
        else { break; }
    }
}

void swim(int i)
{
    while (i > 1 && pq[i/2] < pq[i])  // while parent is less than child
    {
        swap(i, i/2);  // swap parent and child
        i = i/2; // swim up tree
    }
}

void swap(int i, int j)
{
    int temp = pq[i];
    pq[i] = pq[j];
    pq[j] = temp;
}

void show_items(int *arr, int n)
{
    printf("[");
    for (int i = 0; i < n; i++)
    {
        if (i == n - 1)
        {
            printf("%i]\n", arr[i]);
            break;
        }
        printf("%i, ", arr[i]);
    }
}