package InterviewProblems.ReverseArray;

import java.util.Arrays;
/*
Problem:
Reverse an array in place using no extra memory in O(N) time
*/

public class ReverseArray {

    public static void reverseArray(Object[] arr) {
        int i = 0;              // pointer to beginning of arr
        int j = arr.length - 1; // pointer to end or arr
        while (i < j) {
            swap(arr, i, j);
            i++;
            j--;
        }
    }

    private static void swap(Object[] arr, int i, int j) {
        Object t = arr[i];
        arr[i] = arr[j];
        arr[j] = t;
    }

    // Test Client
    public static void main(String[] args) {
        String[] test1 = {"A", "B", "C", "D", "E", "F", "G", "H"};  // even # of items
        Integer[] test2 = {1, 2, 3, 4, 5, 6, 7, 8, 9};              // odd # of items
        ReverseArray.reverseArray(test1);
        ReverseArray.reverseArray(test2);
        System.out.println(Arrays.toString(test1));
        System.out.println(Arrays.toString(test2));
    }
}