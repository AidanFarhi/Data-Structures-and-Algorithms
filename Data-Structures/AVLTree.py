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
    def __init__(self, data, parent=None):
        self.data = data
        self.left = None
        self.right = None
        self.parent = parent
        self.count = 1
        self.height = 0


class AVLTree:
    def __init__(self):
        self.root = None

    def __get_height(self, node):
        return -1 if node is None else node.height

    def __get_balance(self, node):
        return 0 if node is None else self.__get_height(node.left) - self.__get_height(node.right)

    def __set_height(self, node):
        node.height = max(self.__get_height(node.left), self.__get_height(node.right)) + 1

    def insert(self, data):
        if self.root is not None:
            self.__insert_helper(self.root, data)
        else:
            self.root = Node(data)

    def __insert_helper(self, node, data):
        if node.data > data:
            if node.left:
                self.__insert_helper(node.left, data)
            else:
                node.left = Node(data, node)
                self.__handle_violation(node)
        elif node.data < data:
            if node.right:
                self.__insert_helper(node.right, data)
            else:
                node.right = Node(data, node)
                self.__handle_violation(node)
        else:
            node.count += 1

    def __handle_violation(self, node):
        while node:
            self.__set_height(node)
            self.__handle_violation_helper(node)
            node = node.parent

    def __handle_violation_helper(self, node):
        balance = self.__get_balance(node)
        if balance < -1:  # Left heavy
            if self.__get_balance(node.right) > 0:  # LR heavy
                self.__rotate_right(node.right)
            self.__rotate_left(node)
        if balance > 1:  # Right heavy
            if self.__get_balance(node.left) < 0:  # RL heavy
                self.__rotate_left(node.left)
            self.__rotate_right(node)

    def __rotate_right(self, node):
        t_left = node.left
        t = t_left.right
        t_left.right = node
        node.left = t
        if t is not None:
            t.parent = node
        t_parent = node.parent
        node.parent = t_left
        t_left.parent = t_parent
        if t_parent and t_parent.right == node:
            t_parent.right = t_left
        if t_parent and t_parent.left == node:
            t_parent.left = t_left
        if node == self.root:
            self.root = t_left
        self.__set_height(node)
        self.__set_height(t_left)

    def __rotate_left(self, node):
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
        if t_parent and t_parent.left == node:
            t_parent.left = t_right
        if node == self.root:
            self.root = t_right
        self.__set_height(node)
        self.__set_height(t_right)

    def show_nodes_in_order(self):
        if self.root:
            arr = []
            self.__show_nodes_in_order_helper(self.root, arr)
            print(arr)

    def __show_nodes_in_order_helper(self, node, arr):
        if node.left:
            self.__show_nodes_in_order_helper(node.left, arr)
        for _ in range(node.count):
            arr.append(node.data)
        if node.right:
            self.__show_nodes_in_order_helper(node.right, arr)

    def get_tree_height(self):
        if self.root:
            print("Tree height:", self.__get_tree_height_helper(self.root))
        else:
            print("Tree is empty")

    def __get_tree_height_helper(self, node):
        return -1 if node is None else 1 + max(self.__get_tree_height_helper(node.left), self.__get_tree_height_helper(node.right))

    def delete_value(self, value):
        if self.root:
            self.__delete_value_helper(self.root, value)

    def __delete_value_helper(self, node, value):
        if node.data > value:
            if node.left:
                self.__delete_value_helper(node.left, value)
        if node.data < value:
            if node.right:
                self.__delete_value_helper(node.right, value)
        if node.data == value:
            parent = node.parent
            if node.left is None and node.right is None:
                if parent:
                    if parent.left == node:
                        parent.left = None
                    if parent.right == node:
                        parent.right = None
            if node.left is None and node.right is not None:
                if parent:
                    if parent.left == node:
                        parent.left = node.right
                    if parent.right == node:
                        parent.right = node.right
                    node.right.parent = parent
                else:
                    node.right = self.root
                    node.right.parent = None
            if node.left is not None and node.right is None:
                if parent:
                    if parent.left == node:
                        parent.left = node.left
                    if parent.right == node:
                        parent.right = node.left
                    node.left.parent = parent
                else:
                    node.left = self.root
                    node.left.parent = None
            if node.left is not None and node.right is not None:
                predecessor = self.__get_predecessor(node.left)
                t_data = node.data
                node.data = predecessor.data
                predecessor.data = t_data
                self.__delete_value_helper(predecessor, value)
            if parent:
                self.__handle_violation(parent)

    def __get_predecessor(self, node):
        return self.__get_predecessor(node.right) if node.right else node

    def has_value(self, value):
        if self.root:
            return self.__has_value_helper(self.root, value)

    def __has_value_helper(self, node, value):
        if node.data > value:
            if node.left:
                return self.__has_value_helper(node.left, value)
            else:
                return False
        if node.data < value:
            if node.right:
                return self.__has_value_helper(node.right, value)
            else:
                return False
        if node.data == value:
            return True

    def get_max(self):
        if self.root:
            print("Max value:", self.__get_max_helper(self.root))

    def __get_max_helper(self, node):
        return self.__get_max_helper(node.right) if node.right else node.data

    def get_min(self):
        if self.root:
            print("Min value:", self.__get_min_helper(self.root))

    def __get_min_helper(self, node):
        return self.__get_min_helper(node.left) if node.left else node.data


# - TESTS -
avl_tree = AVLTree()
for i in range(10):
    avl_tree.insert(i)

avl_tree.show_nodes_in_order()
avl_tree.get_tree_height()
avl_tree.get_max()
avl_tree.get_min()
print("Has value 5:", avl_tree.has_value(5))
