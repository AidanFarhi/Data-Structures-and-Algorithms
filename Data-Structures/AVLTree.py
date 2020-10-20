"""
- AVL Tree -

- A binary tree structure in which the heights of both
  subtrees of a given node are constantly checked after insertions
  and 'balanced' so that all operations will not exceed
  O(log N).
  This is achieved by repeated rotations (either left or right).
- The heights of each child subtree cannot differ by more than one

               + Running Times +
        - Average -      - Worst Case -
Space       O(N)             O(N)
Insert      O(log N)         O(log N)
Delete      O(log N)         O(log N)
Search      O(log N)         O(log N)

Applications
- AVL Sort: O(N * log N) - Downside: Uses more memory than QuickSort -
- Databases where deletions or insertions are not so frequent
  but you have to make a lot of lookups
- Look-up tables are usually implemented with the help of
  hash tables but AVL trees support more operations in the main
- red-black trees are a bit more popular because for AVL trees we
  have to make several rotations - a bit slower -
"""


class Node:
    def __init__(self, data, parent):
        self.data = data
        self.parent = parent
        self.left = None
        self.right = None
        self.height = 0


class AVLTree:
    def __init__(self):
        self.root = None

    def get_height(self, node):
        return -1 if node is None else node.height

    def get_balance(self, node):
        return 0 if node is None else self.get_height(node.left) - self.get_height(node.right)

    def set_height(self, node):
        return max(self.get_height(node.right), self.get_height(node.left)) + 1

    def insert(self, data):
        if self.root is None:
            self.root = Node(data, None)
        else:
            self.insert_helper(self.root, data)

    def insert_helper(self, node, data):
        if node.data > data:
            if node.left is None:
                node.left = Node(data, node)
                node.height = self.set_height(node)
            else:
                self.insert_helper(node.left, data)
        else:
            if node.right is None:
                node.right = Node(data, node)
                node.height = self.set_height(node)
            else:
                self.insert_helper(node.right, data)
        self.handle_violation(node)

    def handle_violation(self, node):
        while node:
            node.height = self.set_height(node)
            self.handle_violation_helper(node)
            node = node.parent

    def handle_violation_helper(self, node):
        balance = self.get_balance(node)
        if balance < -1:  # Right heavy
            if self.get_balance(node.right) > 0:  # RL heavy
                self.rotate_right(node.right)
            self.rotate_left(node)
        if balance > 1:  # Left Heavy
            if self.get_balance(node.left) < 0:  # LR Heavy
                self.rotate_left(node.left)
            self.rotate_right(node)

    def rotate_right(self, node):
        print('rotating right')
        t_left = node.left
        t = t_left.right
        t_left.right = node
        node.left = t
        if t is not None:
            t.parent = node
        t_parent = node.parent
        node.parent = t_left
        t_left.parent = t_parent
        if t_parent and t_parent.right == node:  # Node was a right child
            t_parent.right = t_left
        elif t_parent and t_parent.left == node:  # Node was a left child
            t_parent.left = t_left
        else:
            if node == self.root:
                self.root = t_left
        node.height = self.set_height(node)
        t_left.height = self.set_height(t_left)

    def rotate_left(self, node):
        print('rotating left')
        t_right = node.right
        t = t_right.left
        t_right.left = node
        node.right = t
        if t is not None:
            t.parent = node
        t_parent = node.parent
        node.parent = t_right
        t_right.parent = t_parent
        if t_parent and t_parent.right == node:
            t_parent.right = t_right
        elif t_parent and t_parent.left == node:
            t_parent.left = t_right
        else:
            if node == self.root:
                self.root = t_right
        node.height = self.set_height(node)
        t_right.height = self.set_height(t_right)

    def remove(self, value):
        if self.root:
            self.remove_helper(self.root, value)

    def remove_helper(self, node, value):
        if node.data > value:
            if node.left:
                self.remove_helper(node.left, value)
        elif node.data < value:
            if node.right:
                self.remove_helper(node.right, value)
        else:
            parent = node.parent
            if not node.right and not node.left:
                if parent and parent.right == node:
                    parent.right = None
                elif parent and parent.left == node:
                    parent.left = None

                else:
                    self.root = None
                del node
                self.handle_violation(parent)
            elif not node.right and node.left:
                if parent and parent.right == node:
                    parent.right = node.left
                    node.left.parent = parent
                elif parent and parent.left == node:
                    parent.left = node.left
                    node.left.parent = parent
                else:
                    self.root = node.left
                    node.left.parent = None
                del node
                self.handle_violation(parent)
            elif node.right and not node.left:
                if parent and parent.right == node:
                    parent.right = node.right
                    node.right.parent = parent
                elif parent and parent.left == node:
                    parent.left = node.right
                    node.right.parent = parent
                else:
                    self.root = node.right
                    node.right.parent = None
                del node
                self.handle_violation(parent)
            else:
                predecessor = self.get_predecessor(node.left)
                t_data = predecessor.data
                predecessor.data = node.data
                node.data = t_data
                self.remove_helper(predecessor, value)

    def get_predecessor(self, node):
        if node.right:
            return self.get_predecessor(node.right)
        return node

    def traverse(self):
        if self.root:
            self.traverse_in_order(self.root)

    def traverse_in_order(self, node):
        if node.left:
            self.traverse_in_order(node.left)
        print(node.data)
        if node.right:
            self.traverse_in_order(node.right)

    def get_max(self):
        n = self.root
        while n.right:
            n = n.right
        return n.data

    def get_min(self):
        n = self.root
        while n.left:
            n = n.left
        return n.data


avl = AVLTree()
for i in range(-100, 500):
    avl.insert(i)

print(f'Max: {avl.get_max()}')
print(f'Min: {avl.get_min()}')
print(f'Root: {avl.root.data}')
avl.traverse()