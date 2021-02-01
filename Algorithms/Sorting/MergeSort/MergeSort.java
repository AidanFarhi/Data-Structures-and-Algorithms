package Algorithms.Sorting.MergeSort;

import java.util.Arrays;

public class MergeSort {

    public static void sort(Comparable[] arr) {
        // Create aux array here before recursion to boost performance
        Comparable[] aux = new Comparable[arr.length];  
        sortHelper(arr, aux, 0, arr.length - 1);
    }

    private static void sortHelper(Comparable[] arr, Comparable[] aux, int lo, int hi) {
        if (hi <= lo) return;
        int mid = lo + (hi - lo) / 2;
        sortHelper(arr, aux, lo, mid);
        sortHelper(arr, aux, mid + 1, hi);
        merge(arr, aux, lo, mid, hi);
    }

    private static void merge(Comparable[] arr, Comparable[] aux, int lo, int mid, int hi) {
        // First copy items into aux array 
        for (int n = lo; n <= hi; n++) {
            aux[n] = arr[n];
        }
        // Now merge two sorted halves
        int i = lo, j = mid + 1;
        for (int n = lo; n <= hi; n++) {
            if (i > mid) arr[n] = aux[j++];     // If left half of array is exhausted
            else if (j > hi) arr[n] = aux[i++]; // If right half of array is exhausted
            else if (lessThan(aux[i], aux[j])) arr[n] = aux[i++];
            else arr[n] = aux[j++]; 
        } 
    }

    private static boolean lessThan(Comparable a, Comparable b) {
        return a.compareTo(b) < 0;
    }

    public static void main(String[] args) {
        String[] test1 = {"bibs", "zoo", "loss", "friend", "abby", "allan", "knife", "were", "waa", "loss"};
        Integer[] test2 = {6, 1, 7, 3, 4, 11, -66, 141, 664, -26, 1616, 2, 88, 1, 755, -2, -66, -2777};
        MergeSort.sort(test1);
        MergeSort.sort(test2);
        System.out.println(Arrays.toString(test1));
        System.out.println(Arrays.toString(test2));
    }
}