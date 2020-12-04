"""
- Array -

A contiguous area of memory consisting of
equal-size elements indexed by contiguous integers

Positives:
- Adding, Searching is a fast operation
- Random access is possible
- Can construct multidimensional arrays (matrix)

Negatives:
- Have to know the size of array at compile time
- Not able to store items with different value types (Java, C++, C)
- If array is full, you have to copy the all
  the contents of the array first and then resize, which takes O(N).

Applications:
- lookup tables
- hash tables
- heaps

Operations:
- size() -> returns current size
- capacity() -> returns capacity
- is_empty() -> returns if empty or not
- item_at(index) -> returns the item at a given index
- push(item) -> adds item to end of array
- insert_item(index, item) -> inserts item at index, then shifts elements to the right
- prepend(item) -> adds item to front of array
- pop() -> removes and returns item at end of array
- delete(index) -> removes item at given index, then shifts elements to the left
- remove(item) -> removes all occurrences of given item
- find(item) -> returns first index where item is found or -1 if not found
- resize(new_capacity) (Private method) -> if array is at capacity, then double size, if array is 1/4 full,
  half the capacity

Times for Common Operations:

        Add   |   Remove
    -----------------------
Beg |  O(N)   |   O(N)
    -----------------------
Mid |  O(N)   |   O(N)
    -----------------------
End |  O(1)   |   O(1)
    -----------------------
"""


class Array:

    def __init__(self):
        self.size = 0
        self.capacity = 16
        self.arr = [None] * 16

    def get_size(self):
        return self.size

    def get_capacity(self):
        return self.capacity

    def is_empty(self):
        return self.size == 0

    def item_at(self, index):
        if index < self.capacity:
            return self.arr[index]
        else:
            raise IndexError('Index out of range')

    def push(self, item):
        if self.size < self.capacity:
            self.arr[self.size] = item
            self.size += 1
        else:
            print(f'Increasing capacity to: {self.capacity * 2}')
            self.__resize(self.capacity * 2)
            self.arr[self.size] = item
            self.size += 1

    def __resize(self, new_capacity):
        new_arr = [None] * new_capacity
        i = 0
        for k in range(self.size):
            new_arr[i] = self.arr[k]
            i += 1
        self.arr = new_arr
        self.capacity = new_capacity

    def insert_item(self, index, item):
        if index == 0:
            self.prepend(item)
            return
        elif index > self.size:
            raise IndexError('Index out of range')
        elif index == self.size:
            self.push(item)
            return
        if self.size == self.capacity:
            self.__resize(self.capacity * 2)
        i = self.size
        while i > index:
            self.arr[i] = self.arr[i - 1]
            i -= 1
        self.arr[index] = item
        self.size += 1

    def prepend(self, item):
        if self.size == 0:
            self.push(item)
            return
        if self.size == self.capacity:
            self.__resize(self.capacity * 2)
        i = self.size
        while i > 0:
            self.arr[i] = self.arr[i - 1]
            i -= 1
        self.arr[0] = item
        self.size += 1

    def show_items(self):
        print(self.arr)

    def pop(self):
        if self.size > 0:
            data = self.arr[self.size - 1]
            self.arr[self.size - 1] = None
            self.size -= 1
            if self.size <= self.capacity // 4 and self.capacity > 16:
                print(f'Reducing capacity to: {self.capacity // 2}')
                self.__resize(self.capacity // 2)
            return data

    def delete(self, index):
        if index > self.size - 1:
            raise IndexError('Index out of range')
        if self.size > 0:
            i = index
            while i < self.size:
                self.arr[i] = self.arr[i + 1]
                i += 1
            self.size -= 1
        if self.size <= self.capacity // 4 and self.capacity > 16:
            print(f'Reducing capacity to: {self.capacity // 2}')
            self.__resize(self.capacity // 2)

    def find(self, item):
        for i in range(self.size):
            if self.arr[i] == item:
                print('item found at index:', i)
                return i
        print('Item not found')
        return -1

    def remove(self, item):
        if self.size > 0:
            for i in range(self.size):
                if self.arr[i] == item:
                    self.delete(i)
                    self.remove(item)
                    break