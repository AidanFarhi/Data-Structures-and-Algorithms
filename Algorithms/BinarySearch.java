package Algorithms;

public class BinarySearch {

    // Default Constructor
    public BinarySearch() {}

    /*
    Binary Search -> Returns first index found of target or -1 if not found
    */
    public int binarySearch(int[] arr, int target) {
        int lo = 0;
        int hi = arr.length - 1;
        while (lo <= hi) {
            int mid = lo + (hi - lo) / 2;
            if (arr[mid] < target) {
                lo = mid + 1;
            } else if (arr[mid] > target) {
                hi = mid - 1;
            } else {
                return mid;
            } 
        }
        return -1;
    } 

    // Test Client
    public static void main(String[] args) {
        // Test array 100,000,000 length
        int[] testArray = new int[100000000];
        for (int i = 0; i < 100000000; i++) {
            testArray[i] = i;
        }
        // Binary Search Instance
        BinarySearch BS = new BinarySearch();
        // Run Tests
        System.out.println(BS.binarySearch(testArray, 456635));
        System.out.println(BS.binarySearch(testArray, -1515));
        System.out.println(BS.binarySearch(testArray, 636363));
        System.out.println(BS.binarySearch(testArray, 5));
        System.out.println(BS.binarySearch(testArray, 9999999));
        System.out.println(BS.binarySearch(testArray, -535353));
    }
}