"""
- Merge Sort -

- Divide and conquer algorithm
- Comparison Based Algorithm
- A stable sorting algorithm
- Not an in place algorithm
- Usually merge sort is the best option for sorting a linked list

 Runtime Complexity | Memory Complexity 
     O(N logN)              O(N)
"""

def merge_sort(arr):
    # Base case
    if len(arr) == 1:
        return

    # Divide
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    merge_sort(left)
    merge_sort(right)

    # Conquer
    i = 0
    j = 0
    k = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    # If there are elements left in left sub-arr
    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1

    # If there are elements left in right sub-arr
    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1


test = [-53, 22, 644, 3, 1, 1, 1, 455, -45, -22, -64, 2, 77]
merge_sort(test)
print('Merge Sort:', test)