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
- insertAtStart(value) O(1)
- insertAtEnd(value) O(N) * we have to traverse the whole list
- removeStart() O(1)
- removeItem(value) O(N)
"""


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
    def remove(self, data):
        if self.head is None:
            return

        access_node = self.head
        previous_node = None

        while access_node is not None and access_node.data != data:
            previous_node = access_node
            access_node = access_node.nextNode

        # data does not exist - end of list reached
        if access_node is None:
            return
        
        self.numOfNodes -= 1
        # if data found, this his how we remove - set prev node reference to access_node.nextNode
        if previous_node is None:
            self.head = access_node.nextNode
        else:
            previous_node.nextNode = access_node.nextNode

    # O(N)
    def insert_end(self, data):
        self.numOfNodes += 1
        new_node = Node(data)
        access_node = self.head

        if not self.head:
            self.head = new_node
        else:
            while access_node.nextNode is not None:
                access_node = access_node.nextNode

            access_node.nextNode = new_node

    # O(N)
    def size_of_list(self):
        return self.numOfNodes

    # O(N)
    def print_data(self):
        access_node = self.head

        while access_node is not None:
            print(access_node.data)
            access_node = access_node.nextNode
