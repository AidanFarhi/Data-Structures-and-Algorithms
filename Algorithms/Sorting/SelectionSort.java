package Algorithms.Sorting;

import java.util.Arrays;

public class SelectionSort {
    /*
    The idea is to iterate through the array,
    starting from the beginning (i = 0), and find the smallest item in the array.
    Once you find it, you swap it with i,then increment i.

    Running Time: O(N^2)
    Memory: O(1) (In place)
    */

    // By using the Comparable class, we are able to harness
    // each classes built in compareTo() method.
    public static void sort(Comparable[] arr) {
        int n = arr.length;
        for (int i = 0; i < n; i++) {
            int min = i;
            for (int j = i + 1; j < n; j++) {
                if (less(arr[j], arr[min])) {
                    min = j;
                }
            }
            swap(arr, i, min);
        }
    }

    private static boolean less(Comparable a, Comparable b) {
        return a.compareTo(b) < 0;
    }

    private static void swap(Comparable[] arr, int i, int j) {
        Comparable swap = arr[i];
        arr[i] = arr[j];
        arr[j] = swap;
    }
    
    // Test Client
    public static void main(String[] args) {
        String[] strings = {"Dog", "Man", "Apple", "Friend", "Zoo"};
        Integer[] integers = {-43, 3, 3, 555, 1, 44, 533, -664};
        Double[] doubles = {0.44, 13.55, 535.66, -53.22, -44.55, 23.5, 23.5, 36.5, 1555.66};
        SelectionSort.sort(strings);
        SelectionSort.sort(integers);
        SelectionSort.sort(doubles);
        System.out.println(Arrays.toString(strings));
        System.out.println(Arrays.toString(integers));
        System.out.println(Arrays.toString(doubles));
    }
}
