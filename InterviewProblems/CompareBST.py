# Write a function that checks whether the topology and 
# values of two binary search trees are identical

class Node:
    def __init__(self, data, parent):
        self.data = data
        self.left = None
        self.right = None


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


def compare_trees(node1, node2):
    if not node1 or not node2:
        return node1 == node2
    
    if node1.data != node2.data:
        return False
    
    return compare_trees(node1.left, node2.left) and compare_trees(node1.right, node2.right)

Tree1 = BST()
Tree2 = BST()
Tree3 = BST()
Tree4 = BST()

arr1 = [5, 1, 77, 32, 6, -11, 777]
arr2 = [1, 77, 5, -11, 32, 6, 777]

for num in arr1:
    Tree1.insert(num)
    Tree2.insert(num)
    Tree3.insert(num)

for num in arr2:
    Tree4.insert(num)

print(compare_trees(Tree1.root, Tree2.root))
print(compare_trees(Tree1.root, Tree3.root))
print(compare_trees(Tree3.root, Tree4.root))