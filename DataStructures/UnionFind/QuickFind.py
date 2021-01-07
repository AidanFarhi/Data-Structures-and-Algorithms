import os

"""
- QuickFind Disjointed Set -

Running Times
-------------
connected(x, y) -> O(1)
union(x, y) -> O(N)
"""


class QuickFind:

    # Constructor - Takes in amount of items as an argument
    def __init__(self, items):
        # Maintain a list of roots for every item.
        self.roots = list(range(0, items))  # Each item is initialized as its own root.

    def connected(self, x, y):
        self.__check_input(x, y)
        return self.roots[x] == self.roots[y]

    def union(self, x, y):
        self.__check_input(x, y)
        # Get roots
        x_root = self.roots[x]
        y_root = self.roots[y]
        for i, root in enumerate(self.roots):  # Make all y_roots == x_root
            if root == y_root:
                self.roots[i] = x_root

    def show_roots(self):
        print(self.roots)

    # Throws Exception if arguments are out of range
    def __check_input(self, x, y):
        if x < 0 or x >= len(self.roots) or y < 0 or y >= len(self.roots):
            raise Exception("Item not in set.")
    

# Test section
def main():
    test_file = open(os.getcwd() + '/Tests/UF10.txt', 'r')
    qf = QuickFind(int(test_file.readline())) # Creates a QF object of size 10
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
    qf.show_roots()

main()