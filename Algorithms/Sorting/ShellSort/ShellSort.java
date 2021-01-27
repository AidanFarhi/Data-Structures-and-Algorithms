package Algorithms.Sorting.ShellSort;

import java.util.Arrays;
/* 
* - Shellsort is fast unless array size is very large
* - Very small code footprint, usefull for embedded systems
* - Hardware sort prototype
*/
public class ShellSort {

    public static void sort(Comparable[] arr) {
        int N = arr.length;
        int H = 1;
        // Find max increment start point using Knuth's 3x + 1 formula
        while (H < N / 3) {
            H = 3 * H + 1;  // 1, 4, 13, 40, 121 ...
        }
        // Now H sort the array. Basically insertion sort with a varying increment
        while (H >= 1) {
            // Insertion Sort
            for (int i = H; i < N; i++) {
                for (int j = i; j >= H; j -= H) {
                    if (lessThan(arr[j], arr[j - H])) {
                        swap(arr, j, j - H);
                    } else {
                        break;
                    }
                }
            } 
            // Decrement H
            H = H / 3;
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
        ShellSort.sort(test1);
        ShellSort.sort(test2);
        System.out.println(Arrays.toString(test1));
        System.out.println(Arrays.toString(test2));
    }
}