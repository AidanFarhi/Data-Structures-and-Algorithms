"""

- Bubble Sort -

Iterate through the array, compare each pair of adjacent items,
and swap them if they are in the wrong order.

- Worst Case Running Time: O(n^2)
- Stable (Maintains relative order of elements)
- In place (No extra memory)

"""


def bubble_sort(arr):
    for i in range(len(arr) - 1):
        for j in range(0, len(arr) - 1 - i, 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


test = [-2, 5, 2, -66, 23, -6, 144, 36]
bubble_sort(test)
print(test)