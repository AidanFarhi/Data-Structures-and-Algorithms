class BST:

    class Node:
        def __init__(self, key, val):
            self.key = key
            self.val = val
            self.left = None
            self.right = None

    def __init__(self):
        self.root = None
    
    def put(self, key, val):
        self.root = self.__put_helper(self.root, key, val)

    def __put_helper(self, node, key, val):
        if node is None:
            return BST.Node(key, val)
        if key < node.key:
            node.left = self.__put_helper(node.left, key, val)
        elif key > node.key:
            node.right = self.__put_helper(node.right, key, val)
        else:  # key already exists, so we replace the value
            node.val = val
        return node
    
    def get(self, key):
        node = self.root
        while node is not None:
            if key < node.key:
                node = node.left
            elif key > node.key:
                node = node.right
            else:
                return node.val
        return None

    def get_max(self):
        return self.__get_max_helper(self.root)
    
    def __get_max_helper(self, node):
        if node.right is None:
            return node
        return self.__get_max_helper(node.right)

    def get_min(self):
        return self.__get_min_helper(self.root)
    
    def __get_min_helper(self, node):
        if node is None:
            return None
        elif node.left is None:
            return node
        else:
            return self.__get_min_helper(node.left)

    def delete_min(self):
        self.root = self.__delete_min_helper(self.root)

    def __delete_min_helper(self, node):
        if node.left is None:
            return node.right
        node.left = self.__delete_min_helper(node.left)
        return node

    def delete(self, key):
        self.root = self.__delete_helper(self.root, key)

    def __delete_helper(self, node, key):
        if node is None:
            return None
        if key < node.key:
            node.left = self.__delete_helper(node.left, key)
        elif key > node.key:
            node.right = self.__delete_helper(node.right, key)
        else:
            if node.right is None:  # Case where node has only a left child
                return node.left
            if node.left is None:  # Case where node has only a right child
                return node.right
            # Case where node has two children
            temp = node  # save reference to node
            node = self.__get_min_helper(temp.right)  # replace ref of node with successor
            node.right = self.__delete_min_helper(temp.right)  # delete successor from original place in tree
            node.left = temp.left  # put deleted nodes children onto successor
        return node
    
    def get_keys_in_order(self):
        keys = []
        self.__get_keys_in_order_helper(self.root, keys)
        return keys

    def __get_keys_in_order_helper(self, node, keys):
        if node is None:
            return
        if node.left is not None:
            self.__get_keys_in_order_helper(node.left, keys)
        keys.append(node.key)
        self.__get_keys_in_order_helper(node.right, keys)

    def get_vals_in_order(self):
        vals = []
        self.__get_vals_in_order_helper(self.root, vals)
        return vals

    def __get_vals_in_order_helper(self, node, vals):
        if node is None:
            return
        if node.left is not None:
            self.__get_vals_in_order_helper(node.left, vals)
        vals.append(node.val)
        self.__get_vals_in_order_helper(node.right, vals)
    

def main():

    test = {
        "56": "Bob",
        "100": "Joe",
        "78": "Fred",
        "1": "Al",
        "35": "Greg",
        "90": "Yori",
        "16": "Nola",
        "85": "Dia",
        "2": "Francis",
        "37": "Blob",
        "22": "Zebo"
    }

    bst = BST()

    for key, val in test.items():
        bst.put(int(key), val)

    bst.delete(16)
    bst.delete(2)

    print(bst.get_vals_in_order())
    print(bst.get_keys_in_order())
    print(bst.get(22))
    print(bst.get(100))

main()
