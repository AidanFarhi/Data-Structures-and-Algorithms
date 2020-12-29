"""
- Counting Sort -

- Operates by counting the number of objects that have each distinct
  value key.
- The values have to be non-negative integers
- Only suitable when the variation in keys in not significantly greater 
  than the number of items. 
- It can outperform comparison based sorting algorithms

    | Runtime Complexity   |   Memory Complexity |
          O(N + K + 1)     |         O(K + 1) 
            K == max       |         K == max
        
"""


def counting_sort(arr):

    # Initialize counts array
    counts = [0] * (max(arr) + 1)  # O(N + Max + 1)

    # Populate counts array
    for num in arr:
        counts[num] += 1

    # Rearrange original array to sorted order
    i = 0
    for j, count in enumerate(counts):
        if count > 0:
            for _ in range(count):
                arr[i] = j
                i += 1

    return arr


test = [9, 6, 6, 2, 24, 2, 7, 0, 0, 25, 0, 0, 3]

print(counting_sort(test))
