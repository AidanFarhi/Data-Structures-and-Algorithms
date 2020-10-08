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

# Max number of items that can be stored in heap
CAPACITY = 10


class Heap:
    def __init__(self):
        # Create an array of CAPACITY length
        self.heap = [0] * CAPACITY
        # Keep track of heap size
        self.size = 0

    # Insertion takes O(1) running time, BUT we have to make sure that
    # the heap properties are no violated: fix_up() takes O(logN)
    def insert(self, item):
        # We cannot insert items if capacity is at limit
        if CAPACITY == self.size:
            return
        # Insert item and then increment the counter
        self.heap[self.size] = item
        self.size += 1
        # Now we check if heap properties have been violated
        # starting at last item inserted
        self.fix_up(self.size - 1)

    # Running time: O(logN)
    def fix_up(self, index):
        parent_index = (index - 1) // 2
        if index > 0 and self.heap[index] > self.heap[parent_index]:
            self.swap(index, parent_index)
            self.fix_up(parent_index)

    def swap(self, index1, index2):
        self.heap[index2], self.heap[index1] = self.heap[index1], self.heap[index2]

    # Assuming we are using a max heap O(1)
    def get_max(self):
        return self.heap[0]

    # Return and remove max item. O(logN)
    def poll(self):
        maximum = self.get_max()
        self.swap(0, self.size - 1)
        self.size -= 1
        self.fix_down(0)
        return maximum

    def fix_down(self, index):
        # To get the left child
        left_index = index * 2 + 1
        # To get the right child
        right_index = index * 2 + 2
        # Set largest index
        largest_index = index
        # If the left child is greater than the parent: largest is the left node
        if left_index < self.size and self.heap[left_index] > self.heap[index]:
            largest_index = left_index
        # If the right child is greater than the left child: largest is the right node
        if right_index < self.size and self.heap[right_index] > self.heap[largest_index]:
            largest_index = right_index
        # We don't swap items with themselves
        if index != largest_index:
            self.swap(index, largest_index)
            self.fix_down(largest_index)

    # Given N items and we want to sort them with a heap:
    # every poll() takes O(logN)
    # for loop will take O(N)
    # Overall running time is O(NlogN)
    def heap_sort(self):
        size = self.size
        for i in range(0, size):
            maximum = self.poll()
            print(maximum)


heap = Heap()
array = [10, 8, 12, 20, -2, 0, 1, 321]
for num in array:
    heap.insert(num)

heap.heap_sort()
