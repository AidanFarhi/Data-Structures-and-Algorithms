import os

class WeightedQuickUnion:

    def __init__(self, size):
        self.roots = list(range(0, size))
        self.sizes = list(range(0, size))
        for i in range(size):
            self.sizes[i] = 1

    def connected(self, p, q):
        return self.get_root(p) == self.get_root(q)

    def union(self, p, q):
        p_root = self.get_root(p)
        q_root = self.get_root(q)
        if p_root != q_root:
            if self.sizes[p_root] < self.sizes[q_root]:
                self.roots[p_root] = q_root
                self.sizes[q_root] += 1
            else:
                self.roots[q_root] = p_root
                self.sizes[p_root] += 1

    def get_root(self, n):
        while n != self.roots[n]:
            self.roots[n] = self.roots[self.roots[n]]
            n = self.roots[n]
        return n


# Test section
def main():
    test_file = open(os.getcwd() + '/Tests/UF10.txt', 'r')
    wqu = WeightedQuickUnion(int(test_file.readline()))
    pair = test_file.readline()
    while pair:
        p = int(pair[0])
        q = int(pair[2])
        if wqu.connected(p, q):
            print(f'[{p}, {q}] already connected..')
        else:
            wqu.union(p, q)
            print(f'[{p}, {q}] now connected..')
        pair = test_file.readline()

main()