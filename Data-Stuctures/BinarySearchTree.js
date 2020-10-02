class Node {
    constructor(data, parent) {
        this.data = data
        this.parent = parent
        this.left = null
        this.right = null
    }
}
class BST {
    constructor() {
        this.root = null
    }
    insert(data) {
        if (this.root === null) {
            this.root = new Node(data, null)
        } else {
            this.insertHelper(this.root, data)
        }
    }
    insertHelper(node, data) {
        if (node.data > data) {
            if (node.left === null) {
                node.left = new Node(data, node)
            } else {
                this.insertHelper(node.left, data)
            }
        } else {
            if (node.right === null) {
                node.right = new Node(data, node)
            } else {
                this.insertHelper(node.right, data)
            }
        }
    }
    remove(data) {
        if (this.root === null) {
            return
        } else if (this.root.left === null 
            && this.root.right === null 
            && this.root.data === data) {
            this.root = null
        } else {
            this.removeHelper(this.root, data)
        }
    }
    removeHelper(node, data) {
        if (node === null) {
            return
        } else if (node.data > data) {
            this.removeHelper(node.left, data)
        } else if (node.data < data) {
            this.removeHelper(node.right, data)
        } else {
            if (node.right === null && node.left === null) { // Node has no children
                if (node.parent.left === node) { // Node is a left child
                    node.parent.left = null
                } else { // Node is a right child
                    node.parent.right = null
                }
            } else if (node.right !== null && node.left === null) { // Node has one right child
                if (node.parent.left === node) { // Node is a left child
                    node.parent.left = node.right
                    node.right.parent = node.parent
                } else { // Node is a right child
                    node.parent.right = node.right
                    node.right.parent = node.parent
                }
            } else if (node.right === null && node.left !== null) { // Node has one left child
                if (node.parent.left === node) { // Node is a left child
                    node.parent.left = node.left
                    node.left.parent = node.parent
                } else { // Node is a right child
                    node.parent.right = node.left
                    node.left.parent = node.parent
                }
            } else { // Node has two children
                let predecessor = this.get_predecessor(node.left)
                let swap = predecessor.data
                predecessor.data = node.data
                node.data = swap
                this.removeHelper(predecessor)
            }
        }
    }
    get_predecessor(node) {
        if (node.right) {
            return this.get_predecessor(node.right)
        } 
        return node
    }
    traverse() {
        if (this.root === null) {
            return
        } else {
            this.traverseInOrder(this.root)
        }
    }
    traverseInOrder(node) {
        if (node.left) {
            this.traverseInOrder(node.left)
        }
        console.log(node.data)
        if (node.right) {
            this.traverseInOrder(node.right)
        }
    }
    getMax() {
        if (this.root === null) {
            return 
        } else if (this.root.right === null) {
            return this.root.data
        } else {
            return this.getMaxHelper(this.root)
        }
    }
    getMaxHelper(node) {
        if (node.right) {
            return this.getMaxHelper(node.right)
        }
        return node.data
    }
    getMin() {
        if (this.root === null) {
            return 
        } else if (this.root.left === null) {
            return this.root.data
        } else {
            return this.getMinHelper(this.root)
        }
    }
    getMinHelper(node) {
        if (node.left) {
            return this.getMinHelper(node.left)
        }
        return node.data
    }
    hasValue(value) {
        if (this.root === null) {
            return false
        } else if (this.root.data === value) {
            return true
        } else {
            return this.hasValueHelper(this.root, value)
        }
    }
    hasValueHelper(node, value) {
        if (node === null) {
            return false
        } else if (node.data === value) {
            return true
        } else if (node.data > value) {
            return this.hasValueHelper(node.left, value)
        } else {
            return this.hasValueHelper(node.right, value)
        }
    }
}
