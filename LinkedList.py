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
- Doubly linked lists sacrifice memory for the ability to navigate backwards.

Applications:
- Stacks
- Queues

Operations:
- insertAtStart(value) O(1)
- insertAtEnd(value) O(N) * we have to traverse the whole list
- removeStart() O(1)
- removeItem(value) O(N)
"""

# First implementation


class Node:
    def __init__(self, data):
        self.data = data
        self.nextNode = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.numOfNodes = 0

    # this is why we like linked lists: O(1) to insert at start
    def insert_start(self, data):
        self.numOfNodes += 1
        new_node = Node(data)

        # if there is no head yet
        if not self.head:
            self.head = new_node
        else:
            new_node.nextNode = self.head
            self.head = new_node

    # O(N)
    def insert_end(self, data):
        self.numOfNodes += 1
        new_node = Node(data)

        actual_node = self.head

        while actual_node.nextNode is not None:
            actual_node = actual_node.nextNode

        actual_node.nextNode = new_node

    def size_of_list(self):
        return self.numOfNodes

    def print_data(self):
        actual_node = self.head

        while actual_node is not None:
            print(actual_node.data)
            actual_node = actual_node.nextNode
