import os

class QuickUnion:

    def __init__(self, size):
        """
        Maintain an array of size N.
        Array entry == root
        Index == object id
        """
        self.roots = list(range(0, size))
    
    def connected(self, p, q):
        return self.get_root(p) == self.get_root(q)

    def union(self, p, q):
        p_root = self.get_root(p)
        q_root = self.get_root(q)
        self.roots[q_root] = p_root
    
    def get_root(self, n):
        while n != self.roots[n]:
            n = self.roots[n]
        return n

# Test section
def main():
    test_file = open(os.getcwd() + '/Tests/UF10.txt', 'r')
    qu = QuickUnion(int(test_file.readline()))
    pair = test_file.readline()
    while pair:
        p = int(pair[0])
        q = int(pair[2])
        if qu.connected(p, q):
            print(f'[{p}, {q}] already connected..')
        else:
            qu.union(p, q)
            print(f'[{p}, {q}] now connected..')
        pair = test_file.readline()

main()