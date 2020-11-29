"""
- Insertion Sort -

| Running Time |
    O(N^2)

- Efficient on smaller data sets 10-20 items
- More efficient than Bubble Sort and Selection Sort
- Speeds up when array is already partially sorted
- Stable Algorithm (preserves original order of elements)
- In place algorithm
- In general, insertion sort will write to an array O(N^2) times,
  while selection sort will only write O(N) times. (Better for flash memory)
"""

def insertion_sort(arr):
    for i in range(len(arr)):
        j = i
        while j > 0 and arr[j - 1] > arr[j]:
            temp = arr[j]
            arr[j] = arr[j - 1]
            arr[j - 1] = temp
            j -= 1
    return arr

test1 = [4, 1, 6, 33, 777, 4, 333, 4, -1, 664]
test2 = [-44, 3, -63, 22, 656, -14444, 5, 5, 5]

result1 = insertion_sort(test1)
result2 = insertion_sort(test2)

print(result1)
print(result2)
