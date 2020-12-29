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
- insert(value)
- delete_value(value)
- get_node_count()
- is_in_tree(value)
- show_values_in_order() -> prints an array representation of values in-order.
- get_min()
- get_max()
- get_height()

"""


class Node:

    def __init__(self, data, parent=None):
        self.data = data
        self.parent = parent
        self.left = None
        self.right = None
        self.count = 1


class BST:

    def __init__(self):
        self.root = None
        self.node_count = 0

    def insert(self, data):
        if self.root:
            self.__insert_helper(self.root, data)
        else:
            self.root = Node(data)
        self.node_count += 1

    def __insert_helper(self, node, data):
        if node.data > data:
            if node.left:
                self.__insert_helper(node.left, data)
            else:
                node.left = Node(data, node)
        elif node.data < data:
            if node.right:
                self.__insert_helper(node.right, data)
            else:
                node.right = Node(data, node)
        else:  # duplicate value
            node.count += 1

    def get_node_count(self):
        return self.node_count

    def show_values_in_order(self):
        if self.root:
            arr = []
            self.__show_values_helper(self.root, arr)
            print(arr)
        else:
            print('Tree is empty')

    def __show_values_helper(self, node, arr):
        if node.left:
            self.__show_values_helper(node.left, arr)
        for n in range(node.count):
            arr.append(node.data)
        if node.right:
            self.__show_values_helper(node.right, arr)

    def is_in_tree(self, data):
        if self.root:
            return self.__is_in_tree_helper(self.root, data)
        return False

    def __is_in_tree_helper(self, node, data):
        if node is None:
            return False
        elif node.data > data:
            return self.__is_in_tree_helper(node.left, data)
        elif node.data < data:
            return self.__is_in_tree_helper(node.right, data)
        else:
            return True

    def get_min(self):
        if self.root:
            return self.__get_min_helper(self.root)
        return None

    def __get_min_helper(self, node):
        if node.left:
            return self.__get_min_helper(node.left)
        return node.data

    def get_max(self):
        if self.root:
            return self.__get_max_helper(self.root)
        return None

    def __get_max_helper(self, node):
        if node.right:
            return self.__get_max_helper(node.right)
        return node.data

    def get_height(self):
        if self.root:
            return self.__get_height_helper(self.root)
        return 0

    def __get_height_helper(self, node):
        if node is None:
            return -1
        return 1 + max(self.__get_height_helper(node.left), self.__get_height_helper(node.right))

    def delete_value(self, value):
        if self.root:
            self.__delete_value_helper(self.root, value)
            self.node_count -= 1

    def __delete_value_helper(self, node, value):
        if node is None:
            return
        elif node.data > value:
            if node.left:
                self.__delete_value_helper(node.left, value)
        elif node.data < value:
            if node.right:
                self.__delete_value_helper(node.right, value)
        else:  # We have found the node containing the value.
            parent = node.parent
            if node.left is None and node.right is None:
                if parent is not None:
                    if parent.right == node:
                        parent.right = None
                    else:
                        parent.left = None
                else:
                    self.root = None
            elif node.left is None and node.right is not None:
                if parent is not None:
                    if parent.right == node:
                        parent.right = node.right
                        node.right.parent = parent
                    else:
                        parent.left = node.right
                        node.right.parent = parent
                else:
                    self.root = node.right
                    node.right.parent = None
            elif node.left is not None and node.right is None:
                if parent is not None:
                    if parent.right == node:
                        parent.right = node.left
                        node.left.parent = parent
                    else:
                        parent.left = node.left
                        node.left.parent = parent
                else:
                    self.root = node.left
                    node.left.parent = None
            else:
                predecessor = self.__get_predecessor(node.left)
                temp = predecessor.data
                predecessor.data = node.data
                node.data = temp
                self.__delete_value_helper(predecessor, value)

    def __get_predecessor(self, node):
        if node.right:
            return self.__get_predecessor(node.right)
        return node

#       - TESTS -
# bst = BST()
# test = [-13, 54, 33, 767, 252, -666, 3, -76, 2333]
# for i in range(30):
#     bst.insert(random.randint(-100, 100))
# for num in test:
#     bst.insert(num)

# bst.show_values_in_order()
# bst.delete_value(-13)
# bst.show_values_in_order()
