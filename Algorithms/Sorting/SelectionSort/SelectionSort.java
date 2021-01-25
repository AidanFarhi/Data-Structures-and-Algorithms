package Algorithms.Sorting.SelectionSort;

import java.util.Arrays;

class SelectionSort {

    public static void sort(Comparable[] arr) {
        int N = arr.length;
        for (int i = 0; i < N; i++) {
            int min = i;
            for (int j = i + 1; j < N; j++) {
                if (lessThan(arr[j], arr[min])) {
                    min = j;
                }
            }
            swap(arr, i, min);
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
        SelectionSort.sort(test1);
        SelectionSort.sort(test2);
        System.out.println(Arrays.toString(test1));
        System.out.println(Arrays.toString(test2));
    }
}