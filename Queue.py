"""
- Queue -

Abstract data type. FIFO structure (First In First Out).

Applications:
- When a resource is shared with several consumers (threads): we store them in a queue
- CPU scheduling
- When data is transferred asynchronously between two processes
- IO buffers
- Operational research applications or stochastic models rely heavily on queues
- Last page visited
- Undo function in documents
- stack memory stores local variables and function calls

Operations:
- enqueue() O(1) - insert item to end of queue
- dequeue() O(N) - remove item from front of queue
- peek() O(1) - show item at front of queue
"""

class Queue:
    # here we will use an array for the implementation. You can also use a Linked List
    def __init__(self):
        self.queue = []

    # O(1)
    def enqueue(self, data):
        self.queue.append(data)

    # O(N) with an array, O(1) if using a Linked List
    def dequeue(self):
        if self.queue == []:
            return -1

        data = self.queue[0]
        del self.queue[0]
        return data

    # O(1)
    def peek(self):
        return self.queue[0]

    # O(1)
    def queue_size(self):
        return len(self.queue)    

    def is_empty(self):
        return self.queue == []
