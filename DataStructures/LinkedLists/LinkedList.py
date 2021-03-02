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

    # O(1) operation
    def insert_start(self, data):
        self.size += 1
        if self.head is None:
            self.head = Node(data)
        else:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node

    # O(1) operation
    def remove_start(self):
        if self.head is None:
            return None
        self.size -= 1
        data = self.head.data
        self.head = self.head.next
        return data

    # O(N) operation
    def insert_end(self, data):
        if self.head is None:
            self.insert_start(data)
        else:
            self.size += 1
            n = self.head
            while n.next is not None:
                n = n.next
            n.next = Node(data)

    # O(N) operation
    def remove_end(self):
        if self.head is None:
            return
        elif self.size == 1:
            self.remove_start()
        else:
            self.size -= 1
            n = self.head
            prev = None
            while n.next is not None:
                prev = n
                n = n.next
            data = n.data
            prev.next = None
            return data

    def traverse(self):
        n = self.head
        while n is not None:
            print(n.data)
            n = n.next


def main():

    ll = LinkedList()
    ll.insert_start(300)
    ll.insert_start(200)
    ll.insert_start(100)
    ll.insert_end(400)
    ll.insert_end(500)
    ll.insert_end(600)
    ll.traverse()
    print('-------------')
    ll.remove_end()
    ll.remove_end()
    ll.traverse()


main()