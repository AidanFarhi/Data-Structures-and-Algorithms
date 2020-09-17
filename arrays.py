"""
- Array Data Type -

Positives:
- Adding, Searching is a fast operation
- Random access is possible
- Can construct multidimensional arrays (matrix)

Negatives:
- Have to know the size of array at compile time
- Not able to store items with different value types (Java, C++, C)
- If array is full, you have to copy the all
  the contents of the array first, which takes O(N).

Applications:
- lookup tables
- hash tables
- heaps

Operations:
- add(value) O(1) add to next unoccupied index
- insert(value, index) O(N) we have to shift all the items first
- removeLast() O(1) remove last item
- remove(value) O(N) have to shift all items after removal
"""

# basic array construction
array = [10, 3, 7, 5, 6, 33]

# random indexing: indexing starts with 0
print(array[2])

# get all items
print(array[:])

# get first 3 items
print(array[0:3])

# get all except last one
print(array[:-1])

# update a value
array[3] = 100

# remove value by index (returns value)
# if no index is given, it will remove the last item
array.pop(2)

# remove value by value name (first matching item is removed)
array.remove(33)

# remove with del statement (can remove ranges of values) ex: del array[2:5]
del array[0]

# linear search O(N) (finding max item)
maximum = array[0]

for num in array:
    if num > maximum:
        maximum = num

print(maximum)
