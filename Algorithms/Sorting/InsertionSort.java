package Algorithms.Sorting;

import java.util.Arrays;

public class InsertionSort {
    /*
    - Insertion Sort -
    | Running Time |
        O(N^2)

    - Efficient on smaller data sets 10-20 items
    - More efficient than Bubble Sort and Selection Sort
    - Speeds up when array is already partially sorted
    - Stable Algorithm (preserves original order of elements)
    - In place algorithm
    - In general, insertion sort will write to an array O(N^2) times,
      while selection sort will only write O(N) times. (selection better for flash memory)
    */

    public static void sort(Comparable[] arr) {
        int n = arr.length;
        for (int i = 0; i < n; i++) {
            for (int j = i; j > 0; j--) {
                if (less(arr[j], arr[j - 1])) {
                    swap(arr, j, j - 1);
                } else {
                    break;
                }
            }
        }
    }

    public static boolean less(Comparable a, Comparable b) {
        return a.compareTo(b) < 0;
    }

    public static void swap(Comparable[] arr, int i, int j) {
        Comparable temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    }

    // Test Client
    public static void main(String[] args) {
        String[] strings = {"Dog", "Man", "Apple", "Friend", "Zoo"};
        Integer[] integers = {-43, 3, 3, 555, 1, 44, 533, -664};
        Double[] doubles = {0.44, 13.55, 535.66, -53.22, -44.55, 23.5, 23.5, 36.5, 1555.66};
        InsertionSort.sort(strings);
        InsertionSort.sort(integers);
        InsertionSort.sort(doubles);
        System.out.println(Arrays.toString(strings));
        System.out.println(Arrays.toString(integers));
        System.out.println(Arrays.toString(doubles));
    }
}
