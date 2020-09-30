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
        self.right = None
        self.left = None
        self.height = 0


class AVLTree:
    def __init__(self):
        self.root = None

    def get_height(self, node):
        return -1 if node is None else node.height

    def get_balance(self, node):
        return 0 if node is None else self.get_height(node.left) - self.get_height(node.right)

    def insert(self, data):
        if self.root is None:
            self.root = Node(data, None)
        else:
            self.insert_helper(self.root, data)

    def insert_helper(self, node, data):
        if node.data > data:
            if node.left is not None:
                self.insert_helper(node.left, data)
            else:
                node.left = Node(data, node)
                node.height = max(self.get_height(node.left), self.get_height(node.right)) + 1
        else:
            if node.right is not None:
                self.insert_helper(node.right, data)
            else:
                node.right = Node(data, node)
                node.height = max(self.get_height(node.left), self.get_height(node.right)) + 1

        self.handle_violation(node)

    def handle_violation(self, node):
        while node is not None:
            node.height = max(self.get_height(node.left), self.get_height(node.right)) + 1
            self.handle_violation_helper(node)
            node = node.parent

    def handle_violation_helper(self, node):
        balance = self.get_balance(node)
        if balance < -1:  # Right heavy
            if self.get_balance(node.right) > 0:  # RL heavy
                self.rotate_right(node.right)
            self.rotate_left(node)
        if balance > 1:  # Left heavy
            if self.get_balance(node.left) < 0:  # LR heavy
                self.rotate_left(node.left)
            self.rotate_right(node)

    def rotate_right(self, node):
        t_left = node.left
        t = t_left.right
        t_left.right = node
        node.left = t
        if t is not None:
            t.parent = node
        # Swap the parents of rotated nodes
        t_parent = node.parent
        node.parent = t_left
        t_left.parent = t_parent
        # Check if rotated node was a right child, left child, or root node
        if t_left.parent is not None and t_left.parent.left == node:
            t_left.parent.left = t_left
        if t_left.parent is not None and t_left.parent.right == node:
            t_left.parent.right = t_left
        if node == self.root:
            self.root = t_left
        # Update heights
        node.height = max(self.get_height(node.left), self.get_height(node.right)) + 1
        t_left.height = max(self.get_height(t_left.left), self.get_height(t_left.right)) + 1

    def rotate_left(self, node):
        t_right = node.right
        t = t_right.left
        t_right.left = node
        node.right = t
        if t is not None:
            t.parent = node
        # Swap the parents of the rotated nodes
        t_parent = node.parent
        node.parent = t_right
        t_right.parent = t_parent
        # Check if node was a right child, left child or root node
        if t_right.parent is not None and t_right.parent.left == node:
            t_right.parent.left = t_right
        if t_right.parent is not None and t_right.parent.right == node:
            t_right.parent.right = t_right
        if node == self.root:
            self.root = t_right
        # Update heights
        node.height = max(self.get_height(node.right), self.get_height(node.left)) + 1
        t_right.height = max(self.get_height(t_right.right), self.get_height(t_right.left)) + 1

    def remove(self, data):
        if self.root is None:
            return
        else:
            self.remove_helper(self.root, data)

    def remove_helper(self, node, data):
        if node is None:
            return
        elif node.data > data:
            self.remove_helper(node.left, data)
        elif node.data < data:
            self.remove_helper(node.right, data)
        else:
            if node.right is None and node.left is None:  # Leaf node
                if node.parent.left == node:
                    node.parent.left = None
                elif node.parent.right == node:
                    node.parent.right = None
                else:
                    self.root = None

                parent = node.parent
                del node
                self.handle_violation(parent)
            elif node.right is None and node.left is not None:  # Node has left child
                if node.parent.left == node:
                    node.parent.left = node.left
                    node.left.parent = node.parent
                elif node.parent.right == node:
                    node.parent.right = node.left
                    node.left.parent = node.parent
                else:
                    self.root = node.left
                    node.left.parent = None

                parent = node.parent
                del node
                self.handle_violation(parent)
            elif node.right is not None and node.left is None:  # Node has right child
                if node.parent.left == node:
                    node.parent.left = node.right
                    node.right.parent = node.parent
                elif node.parent.right == node:
                    node.parent.right = node.right
                    node.right.parent = node.parent
                else:
                    self.root = node.right
                    node.right.parent = None

                parent = node.parent
                del node
                self.handle_violation(parent)
            else:  # Node has two children
                predecessor = self.get_predecessor(node.left)
                temp_data = node.data
                node.data = predecessor.data
                predecessor.data = temp_data
                self.remove_helper(predecessor, data)

    def get_predecessor(self, node):
        if node.right:
            return self.get_predecessor(node.right)
        return node

    def traverse(self):
        if self.root is None:
            return
        else:
            self.traverse_in_order(self.root)

    def traverse_in_order(self, node):
        if node.left:
            self.traverse_in_order(node.left)
        print(node.data)
        if node.right:
            self.traverse_in_order(node.right)

    def get_max(self):
        if self.root is None:
            return
        else:
            return self.get_max_helper(self.root)

    def get_max_helper(self, node):
        while node.right:
            node = node.right
        return node.data

    def get_min(self):
        if self.root is None:
            return
        else:
            return self.get_min_helper(self.root)

    def get_min_helper(self, node):
        while node.left is not None:
            node = node.left
        return node.data
