package Algorithms.Sorting.InsertionSort;

import java.util.Arrays;

/*
- Insertion Sort -

| Running Time |
  Avg: O(N^2)  Best: O(N)

- Efficient on smaller data sets 10-20 items
- More efficient than Bubble Sort and Selection Sort
- Speeds up ( O(N) ) when array is already partially sorted
- Stable Algorithm (preserves original order of elements)
- In place algorithm
- In general, insertion sort will write to an array O(N^2) times,
  while selection sort will only write O(N) times. (selection better for flash memory)
*/

public class InsertionSort {

    public static void sort(Comparable[] arr) {
        int N = arr.length;
        for (int i = 0; i < N; i++) {
            for (int j = i; j > 0; j--) { // Go backwards and swap each element if needed
                if (lessThan(arr[j], arr[j - 1])) { 
                    swap(arr, j, j - 1); 
                } else {
                    break;
                }
            }
        }
    }

    private static boolean lessThan(Comparable a, Comparable b) {
        return a.compareTo(b) < 0;
    }

    private static void swap(Comparable[] arr, int i, int j) {
        Comparable temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    }

    public static void main(String[] args) {
        String[] test1 = {"B", "C", "A", "O", "Y", "W"};
        Integer[] test2 = {1, -5, 11, 515, -66, 157, 434};
        InsertionSort.sort(test1);
        InsertionSort.sort(test2);
        System.out.println(Arrays.toString(test1));
        System.out.println(Arrays.toString(test2));
    }
}