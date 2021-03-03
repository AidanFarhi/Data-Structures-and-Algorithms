# Using a Linked List gives us guaranteed O(1) running time for push() and pop()

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.head = None
        self.size = 0

    def push(self, data):
        new_node = Node(data)
        if self.size == 0:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.size += 1

    def pop(self):
        if self.size == 0:
            return None
        data = self.head.data
        self.head = self.head.next
        self.size -= 1
        return data

    def peek(self):
        if self.size == 0:
            return None
        return self.head.data

    def show_items(self):
        n = self.head
        while n:
            print(f'{n.data}-> ', end='')
            n = n.next
        print()

if __name__ == '__main__':
    st = Stack()
    st.push(100)
    st.push(200)
    st.push(300)
    st.push(400)
    st.show_items()
    print('--------')
    print('Popping item:', st.pop())
    print('Popping item:', st.pop())
    st.show_items()
    st.pop()
    st.pop()
    st.pop()
    print('---------')
    st.push(1000)
    st.push(2000)
    st.push(3000)
    st.show_items()
