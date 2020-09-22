"""
- Stack -

LIFO structure: Last In First Out

Applications
- stack oriented languages
- Graph algorithms: depth-first search
- Finding Euler-Cycles in a graph
- Finding strongly connected components in a graph

* MOST IMPORTANT APPLICATION *
 -| Call Stack |-
- A special region of the memory (in the RAM)
- An abstract data type that stores information about the
  active subroutines/methods/functions of a program
- Details are normally hidden and automatic in high-level
  programming languages
- It keeps track of the point to which each active subroutine should
  return control when it finishes executing
- Stores temporary variables created by each function
"""

class Stack:
    def __init__(self):
        self.stack = []

    # Push an item to the end of the stack: O(1)
    def push(self, data):
        self.stack.append(data)

    # Remove and return item from top of the stack: O(1)
    def pop(self):
        if self.stack == []:
            return -1

        data = self.stack[-1]
        del self.stack[-1]
        return data

    # Look at top item of the stack without removing
    def peek(self):
        return self.stack[-1]

    def stack_size(self):
        return len(self.stack)
    
    def is_empty(self):
        return self.stack == []

    def show_stack(self):
        return self.stack
