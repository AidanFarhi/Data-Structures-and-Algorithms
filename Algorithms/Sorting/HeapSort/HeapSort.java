package Algorithms.Sorting.HeapSort;

import java.util.Arrays;

public class HeapSort {

    public static void sort(Comparable[] arr) {
        int N = arr.length - 1;
        heapify(arr, N);  // first create a heap out of arr
        while (N > 0) {  // now repeatedly move max to end of arr
            swap(arr, 0, N);
            sink(arr, 0, --N); // fix heap on each iteration
        }
    }

    private static void heapify(Comparable[] arr, int N) {
        // we do N/2 here because everything in the right half of array is a subtree of size 1
        for (int k = N/2; k >= 0; k--) {
            sink(arr, k, N);
        }
    }

    private static void sink(Comparable[] arr, int k, int N) {
        while (k*2 <= N) {
            int j = k*2;
            if (j < N && lessThan(arr[j], arr[j + 1])) j++;  // find out which child is greater
            if (lessThan(arr[k], arr[j])) {
                swap(arr, k, j);
                k = j;
            } else {
                break;
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
        Integer[] test1 = {5, 1, -66, 141, 667, -567, 1, 777, 2, 1, -88, 2, 6, 7, 7, -222, 7, 22};
        String[] test2 = {"J", "Y", "B", "N", "Q", "P", "A", "R", "H", "G", "Y", "W", "U", "Z", "K"};
        HeapSort.sort(test1);
        HeapSort.sort(test2);
        System.out.println(Arrays.toString(test1));
        System.out.println(Arrays.toString(test2));
    }
}