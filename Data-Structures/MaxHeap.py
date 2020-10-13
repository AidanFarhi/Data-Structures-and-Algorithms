"""
- Heap -

- It is complete: it cannot be unbalanced. We insert every new item to the next available place
- The heap is one maximally efficient implementation of a priority queue abstract data type
- It has nothing to do with the pool of memory from which dynamically allocated memory is allocated

- Basically a binary tree
- Either min heap or max heap
- Constructed from left to right

Min Heap:
- Parent nodes are always less then or equal to child nodes
- Lowest node is the root
Max Heap:
- Parent nodes are always more than or equal to child nodes
- Highest node is the root

Applications:

- Dijkstra's algorithm, Prims algorithm
"""

class MaxHeap:
    def __init__(self, capacity):
        self.capacity = capacity
        self.heap = [None] * capacity
        self.size = 0

    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def insert(self, item):
        if self.size == self.capacity:
            return
        self.heap[self.size] = item
        self.size += 1
        self.fix_up(self.size - 1)

    def fix_up(self, index):
        p_index = (index - 1) // 2
        if index > 0 and self.heap[index] > self.heap[p_index]:
            self.swap(index, p_index)
            self.fix_up(p_index)

    def poll(self):
        data = self.heap[0]
        self.swap(0, self.size - 1)
        self.size -= 1
        self.fix_down(0)
        return data

    def fix_down(self, index):
        l_index = index * 2 + 1
        r_index = index * 2 + 2
        max_index = index
        if l_index < self.size and self.heap[l_index] > self.heap[max_index]:
            max_index = l_index
        if r_index < self.size and self.heap[r_index] > self.heap[max_index]:
            max_index = r_index
        if max_index != index:
            self.swap(index, max_index)
            self.fix_down(max_index)

    def heap_sort(self):
        for i in range(self.size):
            self.poll()


CAPACITY = 10
heap = MaxHeap(CAPACITY)
array = [10, 8, 12, 20, -2, 0, 1, 321, 44, 55]
for num in array:
    heap.insert(num)

heap.heap_sort()
print('after sort')
print(heap.heap)
print(heap.size)
