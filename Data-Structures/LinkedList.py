"""
- Linked List -

Positives:
- Linked lists are dynamic (arrays have a fixed size).
- It can allocate needed memory in run-time.
- Efficient if we want to manipulate the first elements.
- Easy to implement.
- Can store items with different sizes (arrays assume every item same size).
- Easier for linked list to grow organically.

Negatives:
- Wastes memory because of the references.
- Nodes must be read in order, from the beginning because linked lists
  have sequential access.
- Difficulties arise in linked lists when it comes to reverse traversing.
  Singly linked lists are extremely difficult to navigate backwards.
- Doubly linked lists sacrifice by using extra memory for the ability to navigate backwards.

Applications:
- Stacks
- Queues

Operations:
is_empty() -> O(1)
get_size() -> O(1)
value_at(index) -> O(N)
push_front(item) -> O(1)
pop_front() -> O(1)
push_back(item) -> O(N)
pop_back() -> O(N)
peek_front() -> O(1)
peek_back() -> O(N)
insert_at() -> O(N)
erase(index) -> O(N)
reverse() -> O(N)
remove_value(item) -> O(N)
show_list() -> O(N)
"""


class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None
        self.size = 0

    def get_size(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def value_at(self, index):
        if index >= self.size:
            raise IndexError('Index out of range')
        if self.head:
            i = 0
            node = self.head
            while i < index:
                node = node.next
                i += 1
            return node.data

    def push_front(self, item):
        if self.head is not None:
            new_node = Node(item)
            new_node.next = self.head
            self.head = new_node
        else:
            self.head = Node(item)
        self.size += 1

    def pop_front(self):
        if self.head is not None:
            data = self.head.data
            new_head = self.head.next
            if new_head is not None:
                self.head = new_head
            else:
                self.head = None
            self.size -= 1
            return data

    def push_back(self, item):
        if self.head is not None:
            new_node = Node(item)
            node = self.head
            while node.next:
                node = node.next
            node.next = new_node
            self.size += 1
        else:
            self.head = Node(item)
            self.size += 1

    def pop_back(self):
        if self.head is not None:
            node = self.head
            prev = None
            while node.next:
                prev = node
                node = node.next
            if prev is not None:
                prev.next = None
            else:
                self.head = None
            self.size -= 1

    def peek_front(self):
        return self.head.data

    def peek_back(self):
        if self.head:
            node = self.head
            while node.next is not None:
                node = node.next
            return node.data

    def insert_at(self, index, item):
        if index > self.size:
            raise IndexError('Index out of range')
        if index == self.size:
            self.push_back(item)
            return
        if self.head:
            new_node = Node(item)
            i = 0
            node = self.head
            prev = None
            while i < index:
                prev = node
                node = node.next
                i += 1
            if prev is not None:
                prev.next = new_node
                new_node.next = node
            else:
                new_node.next = self.head
                self.head = new_node
            self.size += 1

    def erase(self, index):
        if index > self.size:
            raise IndexError('Index out of range')
        if index == 0:
            self.pop_front()
            return
        if self.head:
            i = 0
            node = self.head
            prev = None
            while i < index:
                prev = node
                node = node.next
                i += 1
            if prev is not None:
                prev.next = node.next
            else:
                self.head = None
            self.size -= 1

    def reverse(self):
        if self.head and self.head.next is not None:
            node = self.head
            prev = None
            while node:
                next_node = node.next
                node.next = prev
                prev = node
                node = next_node
            self.head = prev

    def remove_value(self, item):
        if self.head:
            node = self.head
            prev = None
            while node:
                if node.data == item:
                    if prev is not None:
                        prev.next = node.next
                        self.size -= 1
                        return
                    else:
                        if self.head.next is not None:
                            self.head = self.head.next
                        else:
                            self.head = None
                        self.size -= 1
                prev = node
                node = node.next

    def show_list(self):
        if self.head:
            display = []
            node = self.head
            while node:
                display.append(node.data)
                node = node.next
            return display
        else:
            return []
