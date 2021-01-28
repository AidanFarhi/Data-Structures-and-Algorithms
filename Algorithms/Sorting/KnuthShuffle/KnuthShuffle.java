package Algorithms.Sorting.KnuthShuffle;

import java.util.Arrays;

public class KnuthShuffle {

    public static void shuffle(Object[] arr) {
        int N = arr.length;
        for (int i = 0; i < N; i++) {
            int rand = (int) ((Math.random() * (N - i)) + i);
            swap(arr, rand, i);
        }
    }

    private static void swap(Object[] arr, int i, int j) {
        Object temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    }

    public static void main(String[] args) {
        String[] test1 = {"A", "B", "C", "D", "E", "F", "G"};
        Integer[] test2 = {1, 2, 3, 4, 5, 6, 7, 8, 9};
        KnuthShuffle.shuffle(test1);
        KnuthShuffle.shuffle(test2);
        System.out.println(Arrays.toString(test1));
        System.out.println(Arrays.toString(test2));
    }
}