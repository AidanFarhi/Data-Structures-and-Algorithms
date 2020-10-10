# A Queue implemented with a Doubly Linked List

class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DLL:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_start(self, data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
            self.tail = new_node
        else:
            new_node = Node(data)
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def remove_start(self):
        if self.head:
            data = self.head.data
            if self.head.next:
                self.head = self.head.next
            else:
                self.head = None
            return data

    def insert_end(self, data):
        if self.tail is None:
            self.insert_start(data)
        else:
            new_node = Node(data)
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def remove_end(self):
        if self.tail:
            data = self.tail.data
            if self.tail.prev:
                self.tail = self.tail.prev
                self.tail.next = None
            else:
                self.head = None
                self.tail = None
            return data

    def check_next(self):
        if self.tail:
            return self.tail.data


class Queue:
    def __init__(self):
        self.queue = DLL()

    def enqueue(self, data):
        self.queue.insert_start(data)

    def dequeue(self):
        return self.queue.remove_end()

    def peek(self):
        return self.queue.check_next()


q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print(q.peek())
print(q.dequeue())
