"""
        - Quick Sort -

    - Running Time Complexity -

  | -Best Case- | -Worst Case- |
    O(N logN)       O(N^2)

- In place O(1) memory
- Not a stable algorithm (Does not maintain original order)
- Widely used in programming languages
- Primitive types - Usually are used with quicksort
- Reference types or objects - Usually used with mergesort
"""

class QuickSort:

    def sort(arr):
        QuickSort.sort_helper(arr, 0, len(arr) - 1)
    
    def sort_helper(arr, lo, hi):
        if hi <= lo:
            return
        p = QuickSort.partition(arr, lo, hi)
        QuickSort.sort_helper(arr, lo, p - 1)
        QuickSort.sort_helper(arr, p + 1, hi)
    
    def partition(arr, lo, hi):
        i = lo
        j = hi
        while True:
            while arr[lo] >= arr[i]: 
                i += 1
                if i == hi:
                    break
            while arr[lo] <= arr[j]:
                j -= 1
                if j == lo:
                    break
            if i >= j:
                break
            arr[j], arr[i] = arr[i], arr[j]
        arr[lo], arr[j] = arr[j], arr[lo]
        return j
        


def main():

    test1 = [5, 1, 66, -15, -66, -1, 66, 77, 167, 2555, -777, 2, 7737, -887, 2, 727, 77]
    test2 = ['B', 'A', 'Y', 'W', 'U', 'E', 'T', 'B', 'B', 'J', 'T', 'Z', 'A']
    QuickSort.sort(test1)
    QuickSort.sort(test2)
    print(test1)
    print(test2)


main()