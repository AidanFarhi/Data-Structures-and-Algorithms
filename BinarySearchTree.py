"""
- Binary Search Tree -

- Data structure
- Keeps the keys in sorted order so that look up and other operations can use
  binary search
- Each comparison allow the operations to skip over half of the tree, so
  that each lookup/insertion/deletion takes time proportional to the logarithm
  of the number of items stored in the tree O(log N)
- This is much better than the linear time O(N) required to find items by key
  in an unsorted array, but slower than the operations in hash tables
- Every node can have at most two children. Left and Right.
  Left child < Parent
  Right child > Parent

             + Running Times +
        - Average -      - Worst Case -
Space       O(N)             O(N)
Insert      O(log N)         O(N)
Delete      O(log N)         O(N)
Search      O(log N)         O(N)

Operations
- insert()
- search()
- delete()
- in_order_traversal() - recursive - left subtree, root node, right subtree
- pre_order_traversal() - recursive - root, left subtree, right subtree
- post_order_traversal() - recursive - left subtree, right subtree, root
"""


class Node:
    def __init__(self, data, parent):
        self.data = data
        self.left = None
        self.right = None
        self.parent = parent


class BST:
    def __init__(self):
        self.root = None

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
        else:
            if node.right is not None:
                self.insert_helper(node.right, data)
            else:
                node.right = Node(data, node)

    def remove(self, data):
        if self.root is None:
            return
        elif self.root.left is None and self.root.right is None and self.root.data == data:
            self.root = None
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
            if node.left is None and node.right is None:  # Node has no children
                if node.parent.left == node:
                    node.parent.left = None
                    del node
                else:
                    node.parent.right = None
                    del node
            elif node.left is None and node.right is not None:  # Node has one right child
                if node.parent.left == node:  # Current node is a left child
                    node.parent.left = node.right
                    node.right.parent = node.parent
                    del node
                else:  # current node is a right child
                    node.parent.right = node.right
                    node.right.parent = node.parent
                    del node
            elif node.left is not None and node.right is None:  # Node has one left child
                if node.parent.left == node:  # Current node is a left child
                    node.parent.left = node.left
                    node.left.parent = node.parent
                    del node
                else:  # Current node is a right child
                    node.parent.right = node.left
                    node.left.parent = node.parent
                    del node
            else:  # Node has two children
                # predecessor will be the largest node in the left sub-tree of Node to delete
                predecessor = self.get_predecessor(node.left)
                temp = predecessor.data
                predecessor.data = node.data
                node.data = temp
                self.remove_helper(predecessor, data)

    def get_predecessor(self, node):
        if node.right:
            return self.get_predecessor(node.right)
        return node

    def traverse(self):
        if self.root is not None:
            self.traverse_in_order(self.root)

    # left subtree, root node, right subtree
    def traverse_in_order(self, node):
        if node.left:
            self.traverse_in_order(node.left)
        print('%s' % node.data)
        if node.right:
            self.traverse_in_order(node.right)

    def get_max(self):
        if self.root is None:
            return
        elif self.root.right is None:
            return self.root.data
        else:
            return self.get_max_helper(self.root)

    def get_max_helper(self, node):
        if node.right is None:
            return node.data
        else:
            return self.get_max_helper(node.right)

    def get_min(self):
        if self.root is None:
            return
        elif self.root.left is None:
            return self.root.data
        else:
            return self.get_min_helper(self.root)

    def get_min_helper(self, node):
        if node.left is None:
            return node.data
        else:
            return self.get_min_helper(node.left)

    def has_value(self, value):
        if self.root is None:
            return False
        elif self.root.data == value:
            return True
        else:
            return self.has_value_helper(self.root, value)

    def has_value_helper(self, node, value):
        if node.data == value:
            return True
        elif node.data > value and node.left is not None:
            return self.has_value_helper(node.left, value)
        elif node.data < value and node.right is not None:
            return self.has_value_helper(node.right, value)
        else:
            return False
