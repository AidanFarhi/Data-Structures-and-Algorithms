"""
- Union Find | Disjoint Set -
"""


class UnionFind:

    # Union: O(N) time | Connected: O(1) time
    class QuickFind:
        def __init__(self, size):
            self.ids = [0] * size
            for i in range(size):
                self.ids[i] = i

        # O(1)
        def connected(self, p, q):
            return self.ids[p] == self.ids[q]

        # O(N)
        def union(self, p, q):
            p_id = self.ids[p]
            q_id = self.ids[q]
            for i, n_id in enumerate(self.ids):
                if n_id == p_id:
                    self.ids[i] = q_id

    # Union: O(N) time | Connected: O(N) time
    class QuickUnion:
        def __init__(self, size):
            self.ids = [0] * size
            for i in range(size):
                self.ids[i] = i

        def get_root(self, i):
            while i != self.ids[i]:
                i = self.ids[i]
            return i

        def connected(self, p, q):
            return self.get_root(p) == self.get_root(q)

        def union(self, p, q):
            p_root = self.get_root(p)
            q_root = self.get_root(q)
            self.ids[p_root] = q_root

    # Union: O(log N) | Connected: O(log N)
    class WeightedQuickUnion:
        def __init__(self, size):
            self.ids = [0] * size
            self.sizes = [0] * size

        def union(self, p, q):
            p_root = self.get_root(p)
            q_root = self.get_root(q)
            if self.sizes[p_root] < self.sizes[q_root]:
                self.ids[p_root] = q_root
                self.sizes[p_root] += self.sizes[q_root]
            else:
                self.ids[q_root] = p_root
                self.sizes[q_root] += self.sizes[p_root]

        def get_root(self, i):
            while i != self.ids[i]:
                i = self.ids[i]
            return i

        def connected(self, p, q):
            return self.get_root(p) == self.get_root(q)