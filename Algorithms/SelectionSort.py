"""
- Selection Sort -

- Running time -
    O(N^2)

- Not stable
- Usually outperforms Bubble Sort
- In place algorithm O(1) memory
- Usefull when auxiliary memory is limited
- Fast for smaller arrays 10-20 items
"""

def selection_sort(arr):
    for i in range(len(arr) - 1):
        index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[index]:
                index = j
        if index != i:
            temp = arr[i]
            arr[i] = arr[index]
            arr[index] = temp
    return arr

test1 = [4, 1, 6, 33, 777, 4, 333, 4, -1, 664]
test2 = [-44, 3, -63, 22, 656, -14444, 5, 5, 5]

result1 = selection_sort(test1)
result2 = selection_sort(test2)

print(result1)
print(result2)
