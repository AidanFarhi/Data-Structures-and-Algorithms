"""
- Red Black Trees -

Rules:
1) Every node has a color either red or black.

2) Root of tree is always black.

3) There are no two adjacent red nodes (A red node cannot have a red parent or red child).

4) Every path from a node (including root) to any of its descendant NULL node has the same number of black nodes.

Same running time as AVL Trees
- Better for insertion operations than AVL trees but not as good for lookups
  because AVL trees are more rigidly balanced
"""


class Color:
    RED = 1
    BLACK = 2


class Node:
    def __init__(self, data, parent=None, color=Color.RED):
        self.data = data
        self.color = color
        self.parent = parent
        self.left = None
        self.right = None


class RedBlackTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if not self.root:
            self.root = Node(data)
            self.check_violation(self.root)
        else:
            self.insert_helper(self.root, data)

    def insert_helper(self, node, data):
        if node.data > data:
            if node.left:
                self.insert_helper(node.left, data)
            else:
                node.left = Node(data, node)
                self.check_violation(node.left)
        else:
            if node.right:
                self.insert_helper(node.right, data)
            else:
                node.right = Node(data, node)
                self.check_violation(node.right)

    def check_violation(self, node):
        while node != self.root and node.parent.color == Color.RED:
            parent = node.parent
            g_parent = parent.parent
            if g_parent is None:
                return
            if parent == g_parent.left:  # parent is left child
                uncle = g_parent.right
                if uncle and uncle.color == Color.RED:  # Case 1 and case 4
                    g_parent.color = Color.RED
                    parent.color = Color.BLACK
                    uncle.color = Color.BLACK
                    node = g_parent
                else:  # Case 2: black uncle
                    if node == parent.right:  # node is a right child
                        self.rotate_left(parent)
                        node = parent
                        parent = node.parent
                    # Case 3
                    parent.color = Color.BLACK
                    g_parent.color = Color.RED
                    self.rotate_right(g_parent)
            else:
                uncle = g_parent.left
                if uncle and uncle.color == Color.RED:  # Case 1 and case 4
                    g_parent.color = Color.RED
                    parent.color = Color.BLACK
                    node = g_parent
                else:  # Case 2: black uncle
                    if node == parent.left:  # node is a left child
                        self.rotate_right(parent)
                        node = parent
                        parent = node.parent
                    parent.color = Color.BLACK
                    g_parent.color = Color.RED
                    self.rotate_left(g_parent)
        if self.root.color == Color.RED:
            self.root.color = Color.BLACK

    def rotate_right(self, node):
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

    def rotate_left(self, node):
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
                self.check_violation(parent)
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
                self.check_violation(parent)
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
                self.check_violation(parent)
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