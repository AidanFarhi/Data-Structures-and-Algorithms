"""
- Double Linked List -

The main difference here is that a double linked list
stores a reference to the next Node AND the previous Node

Positives:
- Can be traversed in both directions
- Removal of data is more efficient if node is given
  ex) For a single linked list, we need the node + previous node vs.
      a double linked list where we only need the node itself

Negatives:
- Uses more memory because of the extra references

Operations:
- insert_start()
- insert_end()
- insert_before()
- insert_after()
- remove_start()
- remove_end()
- remove()
- traverse_list()
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.previous_node = None
        self.next_node = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    # O(1)
    def insert_start(self, data):
        self.size += 1
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
        else:
            new_node.next_node = self.head
            self.head.previous_node = new_node
            self.head = new_node

    # O(N)
    def insert_end(self, data):
        self.size += 1
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
        else:
            access_node = self.head
            while access_node.next_node is not None:
                access_node = access_node.next_node
            access_node.next_node = new_node
            new_node.previous_node = access_node

    # O(N)
    def insert_before(self, given_data, data):
        if self.head is None:
            return 'List is empty'
        else:
            self.size += 1
            access_node = self.head
            while access_node is not None:
                if access_node.data == given_data:
                    break
                access_node = access_node.next_node
            if access_node is None:
                return 'Node not found'
            else:
                new_node = Node(data)
                # if access node is not head
                if access_node.previous_node is not None:
                    new_node.next_node = access_node
                    access_node.previous_node.next_node = new_node
                    new_node.previous_node = access_node.previous_node
                    access_node.previous_node = new_node
                else:
                    new_node.next_node = self.head
                    self.head.previous_node = new_node
                    self.head = new_node

    # O(N)
    def insert_after(self, given_data, data):
        if self.head is None:
            return 'List is empty'
        else:
            self.size += 1
            access_node = self.head
            while access_node is not None:
                if access_node.data == given_data:
                    break
                access_node = access_node.next_node
            if access_node is None:
                return 'Node not found'
            else:
                new_node = Node(data)
                new_node.previous_node = access_node
                new_node.next_node = access_node.next_node
                if access_node.next_node is not None:
                    access_node.next_node.previous_node = new_node
                access_node.next_node = new_node

    def traverse(self):
        if self.size == 0:
            return 'list empty'
        else:
            access_node = self.head
            while access_node is not None:
                print(access_node.data)
                access_node = access_node.next_node

    # O(1)
    def remove_start(self):
        if self.head is None:
            print("The list has no element to delete")
        elif self.head.next_node is None:
            self.head = None
        else:
            self.head = self.head.next_node
            self.head.previous_node = None

    # O(N)
    def remove_end(self):
        if self.head is None:
            print('List empty')
        elif self.head.next_node is None:
            self.head = None
        else:
            access_node = self.head
            while access_node.next_node is not None:
                access_node = access_node.next_node
            access_node.previous_node.next_node = None

    def remove(self, data):
        if self.head is None:
            return 'List empty'
        # case: only one element in list
        elif self.head.next_node is None:
            if self.head.data == data:
                self.head = None
            else:
                return 'Value not found'
        # case: more than one element, and element to delete is at the head
        elif self.head.data == data:
            self.head = self.head.next_node
            self.head.previous_node = None
        else:
            access_node = self.head
            # traverse until data is found or end of list is reached
            while access_node.next_node is not None:
                if access_node.data == data:
                    break
                access_node = access_node.next_node
            # if node to delete is not the last node
            if access_node.next_node is not None:
                access_node.next_node.previous_node = access_node.previous_node
                access_node.previous_node.next_node = access_node.next_node
            else:
                if access_node.data == data:
                    access_node.previous_node.next_node = None
                else:
                    return 'Not found'
