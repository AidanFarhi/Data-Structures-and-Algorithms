package Algorithms.Sorting.QuickSort;
/*
        - Quick Sort -

    - Running Time Complexity -

  | -Best Case- | -Worst Case- |
    O(N logN)       O(N^2)

- In place O(1) memory
- Not a stable algorithm (Does not maintain original order)
- Widely used in programming languages
- Primitive types - Usually are used with quicksort
- Reference types or objects - Usually used with mergesort
*/

import java.util.Arrays;

public class QuickSort {

    public static void sort(Comparable[] arr) {
        sortHelper(arr, 0, arr.length - 1);         // Make call to recursive sortHelper
    }

    private static void sortHelper(Comparable[] arr, int lo, int hi) {
        if (hi <= lo) return;                       // Base case
        int p = partition(arr, lo, hi);
        sortHelper(arr, lo, p - 1);
        sortHelper(arr, p + 1, hi);
    }

    private static int partition(Comparable[] arr, int lo, int hi) {
        int i = lo, j = hi + 1;
        while (true) {
            while (lessThan(arr[++i], arr[lo])) {   // Find item on left to swap
                if (i == hi) break;
            }
            while (lessThan(arr[lo], arr[--j])) {   // Find item on right to swap
                if (j == lo) break;
            }
            if (i >= j) break;                      // Check if pointers have crossed (termination case)
            swap(arr, i, j);                        
        }
        swap(arr, lo, j);                           // Swap with partition element
        return j;                                   // Return index of item that is now in place
    }

    private static void swap(Comparable[] arr, int x, int y) {
        Comparable temp = arr[x];
        arr[x] = arr[y];
        arr[y] = temp;
    }

    private static boolean lessThan(Comparable x, Comparable y) {
        return x.compareTo(y) < 0;
    }

    public static void main(String[] args) {
        Integer[] test1 = {5, 1, -66, 141, 667, -567, 1, 777, 2, 1, -88, 2, 6, 7, 7, -222, 7, 22};
        String[] test2 = {"J", "Y", "B", "N", "Q", "P", "A", "R", "H", "G", "Y", "W", "U", "Z", "K"};
        QuickSort.sort(test1);
        QuickSort.sort(test2);
        System.out.println(Arrays.toString(test1));
        System.out.println(Arrays.toString(test2));
    }
}