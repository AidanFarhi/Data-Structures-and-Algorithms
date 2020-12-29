"""
- Ternary Search Tree -

Every node has three children. left, middle, and right

Advantages:
- TST support sorting
- TST is better than hashing, especially for search misses
- Faster than hashmaps and more flexible than binary search trees
"""

class Node:
    def __init__(self, char):
        self.char = char
        self.left = None
        self.middle = None
        self.right = None
        self.value = None


class TST:
    def __init__(self):
        self.root = None
    
    def insert(self, key, value):
        self.root = self.insert_helper(self.root, key, value, 0)
    
    def insert_helper(self, node, key, value, index):
        ch = key[index]
        if node is None:
            node = Node(ch)
        if node.char < ch:
            node.right = self.insert_helper(node.right, key, value, index)
        elif node.char > ch:
            node.left = self.insert_helper(node.left, key, value, index)
        elif index < len(key) - 1:
            node.middle = self.insert_helper(node.middle, key, value, index + 1)
        else:
            node.value = value
        return node

    def get(self, key):
        node = self.get_helper(self.root, key, 0)
        return node.value if node else None
    
    def get_helper(self, node, key, index):
        ch = key[index]
        if node is None:
            return None
        if node.char < ch:
            return self.get_helper(node.right, key, index)
        elif node.char > ch:
            return self.get_helper(node.left, key, index)
        elif index < len(key) - 1:
            return self.get_helper(node.middle, key, index + 1)
        else:
            return node


tst = TST()
tst.insert('hi', 100)
tst.insert('high', 200)
tst.insert('bye', 400)
tst.insert('goodbye', 900)

print(tst.get('hi'))
print(tst.get('high'))
print(tst.get('hig'))
print(tst.get('bye'))
print(tst.get('goodbye'))
print(tst.get('good'))
