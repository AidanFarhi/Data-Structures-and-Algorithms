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


def quick_sort(arr, low, high):
    if low >= high:
        return

    pivot = partition(arr, low, high)
    quick_sort(arr, low, pivot - 1)
    quick_sort(arr, pivot + 1, high)


def partition(arr, low, high):
    pivot = (low + high) // 2
    swap(arr, pivot, high)
    i = low
    for j in range(low, high):
        if arr[j] <= arr[high]:
            swap(arr, i, j)
            i += 1
    swap(arr, i, high)
    return i


def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]


test1 = [4, 1, 6, 33, 777, 4, 333, 4, -1, 664]
test2 = [-44, 3, -63, 22, 656, -14444, 5, 5, 5]
test3 = [-54, 34, 5, -5, 0, 44, 1414, 6, 6, 343]

quick_sort(test1, 0, len(test1) - 1)
quick_sort(test2, 0, len(test2) - 1)
quick_sort(test3, 0, len(test3) - 1)

print(test1)
print(test2)
print(test3)
