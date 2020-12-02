"""
- Counting Sort -

- Operates by counting the number of objects that have each distinct
  value key.
- The values have to be non-negative integers
- Only suitable when the variation in keys in not significantly greater 
  than the number of items. 
- It can outperform comparison based sorting algorithms

    | Runtime Complexity   |   Memory Complexity |
          O(N + K)         |         O(K) 
      K == max - min + 1   |   K == max - min + 1
        
"""


def counting_sort(arr):
    # Initialize count array
    count_array = [0] * (max(arr) - min(arr) + 1)

    # Count occurrences of each item in array
    for num in arr:
        count_array[num - 1] += 1

    # Populate arr with sorted order
    i = 0
    j = 0
    while i < len(arr):
        while j < len(count_array):
            if count_array[j] > 0:
                num = j + 1
                count = count_array[j]
                k = 0
                while k < count:
                    arr[i] = num
                    i += 1
                    k += 1
            j += 1

    return arr

test = [6, 4, 3, 7, 8, 4, 4, 11, 1, 1, 7]
print(counting_sort(test))
