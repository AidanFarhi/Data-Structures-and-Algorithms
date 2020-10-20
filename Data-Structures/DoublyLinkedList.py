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
        self.next = None
        self.prev = None


class DLL:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_start(self, data):
        if self.head:
            new_node = Node(data)
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        else:
            new_node = Node(data)
            self.head = new_node
            self.tail = new_node

    def remove_start(self):
        if self.head:
            data = self.head.data
            if self.head.next:
                self.head.next.prev = None
                self.head = self.head.next
            else:
                self.head = None
            return data

    def insert_end(self, data):
        if self.tail:
            new_node = Node(data)
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        else:
            self.insert_start(data)

    def remove_end(self):
        if self.tail:
            data = self.tail.data
            if self.tail.prev:
                self.tail.prev.next = None
                self.tail = self.tail.prev
            else:
                self.head = None
                self.tail = None
            return data

    def insert_before(self, node_data, insert_data):
        if self.head.data == node_data:
            self.insert_start(insert_data)
        else:
            node = self.head
            while node:
                if node.data == node_data:
                    new_node = Node(insert_data)
                    node.prev.next = new_node
                    new_node.prev = node.prev
                    node.prev = new_node
                    new_node.next = node
                    return
                node = node.next

    def insert_after(self, node_data, insert_data):
        if self.tail.data == node_data:
            self.insert_end(insert_data)
        else:
            node = self.head
            while node:
                if node.data == node_data:
                    new_node = Node(insert_data)
                    node.next.prev = new_node
                    new_node.next = node.next
                    new_node.prev = node
                    node.next = new_node
                    return
                node = node.next

    def remove(self, val):
        if self.head.data == val:
            self.remove_start()
        elif self.tail.data == val:
            self.remove_end()
        else:
            node = self.head
            while node:
                if node.data == val:
                    node.prev.next = node.next
                    node.next.prev = node.prev
                    return
                node = node.next

    def traverse_backwards(self):
        if self.tail:
            node = self.tail
            while node:
                print(node.data)
                node = node.prev

    def traverse_forwards(self):
        if self.head:
            node = self.head
            while node:
                print(node.data)
                node = node.next
