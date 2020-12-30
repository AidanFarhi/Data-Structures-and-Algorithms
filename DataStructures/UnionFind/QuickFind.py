import os

class QuickFind:
    # Constructor
    def __init__(self, size):
        """
        Maintain an array of size N.
        Array entry == root
        Index == object id
        """
        self.roots = list(range(0, size))
    
    # O(1)
    def connected(self, p, q):
        return self.roots[p] == self.roots[q]
    
    # Set all entries with roots[q] to == roots[p]
    # O(N)
    def union(self, p, q):
        if not self.connected(p, q):
            p_root = self.roots[p]
            q_root = self.roots[q]
            for i, r in enumerate(self.roots):
                if r == q_root:
                    self.roots[i] = p_root
    

# Test section
def main():
    test_file = open(os.getcwd() + '/Tests/UF10.txt', 'r')
    qf = QuickFind(int(test_file.readline()))
    pair = test_file.readline()
    while pair:
        p = int(pair[0])
        q = int(pair[2])
        if qf.connected(p, q):
            print(f'[{p}, {q}] already connected..')
        else:
            qf.union(p, q)
            print(f'[{p}, {q}] now connected..')
        pair = test_file.readline()

main()