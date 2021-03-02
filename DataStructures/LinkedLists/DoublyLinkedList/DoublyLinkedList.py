
class Node:

    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DLL:

    def __init__(self):
        self.head = None
        self.tail = None

    # O(1) operation
    def insert_front(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    # O(1) operation
    def insert_end(self, data):
        new_node = Node(data)
        if self.tail is None:
            self.tail = new_node
            self.head = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    # O(1) operation
    def remove_front(self):
        if self.head is None:
            return None
        data = self.head.data
        if self.head.next is not None:
            self.head.next.prev = None
        self.head = self.head.next
        if self.head is None:  # list is empty now
            self.reset()
        return data

    # O(1) operation
    def remove_end(self):
        if self.tail is None:
            return None
        data = self.tail.data
        if self.tail.prev is not None:
            self.tail.prev.next = None
        self.tail = self.tail.prev
        if self.tail is None:  # list is empty now
            self.reset()
        return data

    def traverse_forward(self):
        n = self.head
        while n:
            print(n.data)
            n = n.next

    def traverse_backward(self):
        n = self.tail
        while n:
            print(n.data)
            n = n.prev

    # method used when list becomes empty after removals
    def reset(self):
        self.head = None
        self.tail = None

# Test Area
def main():
    dll = DLL()
    dll.insert_front(100)
    dll.insert_front(200)
    dll.insert_front(300)
    dll.insert_front(400)
    dll.insert_front(500)
    dll.traverse_forward()
    print('--------')
    dll.traverse_backward()
    print('---------')
    print('removing:', dll.remove_end())
    print('removing:', dll.remove_end())
    dll.traverse_forward()
    print('--------')
    dll.traverse_backward()
    print('-------')
    print('removing:', dll.remove_front())
    print('removing:', dll.remove_front())
    print('removing:', dll.remove_front())
    dll.traverse_forward()
    print('--------')
    dll.traverse_backward()
    print('-----------')
    dll.insert_front(200)
    dll.insert_end(300)
    dll.insert_front(100)
    dll.traverse_forward()
    print('--------')
    dll.traverse_backward()


main()
