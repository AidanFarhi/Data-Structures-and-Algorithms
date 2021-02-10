import os
import sys

# Priority Queue using a binary heap

class MaxPQ:

    def __init__(self, capacity):
        self.pq = [None] * (capacity + 1)
        self.N = 0
    
    def is_empty(self):
        return self.N == 0
    
    def insert(self, item):
        if self.N == len(self.pq) - 1:
            raise Exception(f'pq is at max capacity: {len(self.pq)}')
        self.N += 1
        self.pq[self.N] = item
        self.swim(self.N)

    def get_max(self):
        if self.is_empty():
            raise Exception('pq is empty.')
        return self.pq[1]
    
    def del_max(self):
        if self.is_empty():
            raise Exception('pq is empty.')
        m = self.get_max()
        self.swap(1, self.N) # swap last element and max item
        self.N -= 1  # 'remove' last item
        self.pq[self.N + 1] = None  # prevent loitering
        self.sink(1)
        return m
    
    def sink(self, i):
        while 2*i <= self.N:
            j = 2*i  # left child of i
            if j < self.N and self.pq[j] < self.pq[j + 1]: # find the greater of the two children
                j += 1
            if self.pq[i] < self.pq[j]:  # if parent is less than one of the children, swap
                self.swap(i, j)
                i = j
            else:
                break
    
    def swim(self, i):
        while i > 1 and self.pq[i//2] < self.pq[i]: # while parent (i//2) is less than i
            self.swap(i, i//2)
            i = i//2  # swim up tree

    def swap(self, i, j):
        self.pq[i], self.pq[j] = self.pq[j], self.pq[i]


def main():
    if len(sys.argv) != 2:
        raise Exception('Usage: python3 MaxPQ.py <test file.txt>')
    test = sys.argv[1]
    file = open(os.getcwd() + '/Tests/' + test)
    max_pq = MaxPQ(int(file.readline()))
    line = file.readline()
    while line:
        if line == 'pop\n':
            print(f'max item: {max_pq.del_max()}')
        else:
            max_pq.insert(int(line))
        line = file.readline()
    sorted_arr = [None] * max_pq.N
    for i in range(max_pq.N):
        sorted_arr[i] = max_pq.del_max()
    print(sorted_arr)
    print(len(sorted_arr))
    file.close()


main()