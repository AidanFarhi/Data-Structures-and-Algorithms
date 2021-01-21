# A dynamically resizing stack using an array as an underlying data structure

class ArrayStack:

    # Initialize a stack of size 2 and a pointer the head of the stack along with the capacity
    def __init__(self):
        self.stack = [0] * 2
        self.head = 0
        self.capacity = 2
    
    def push(self, item):
        if self.head == self.capacity:
            self.resize(self.capacity * 2)
        self.stack[self.head] = item
        self.head += 1
    
    def pop(self):
        if self.head == 0:
            return None
        item = self.stack[self.head - 1]
        self.head -= 1
        if self.head > 0 and self.head == self.capacity // 4:
            self.resize(self.capacity // 2)
        return item

    def resize(self, new_capacity):
        self.capacity = new_capacity
        copy = [0] * new_capacity
        for i in range(self.head):
            copy[i] = self.stack[i]
        self.stack = copy

    def show_items(self):
        print(self.stack)


def main():
    s = ArrayStack()
    for i in range(20):
        s.push(i)
    s.show_items()
    for i in range(23):
        print(s.pop())
    s.show_items()


main()