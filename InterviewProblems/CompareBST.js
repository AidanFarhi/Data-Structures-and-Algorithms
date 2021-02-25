// Write a function that checks whether the topology and 
// values of two binary search trees are identical

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
}

function compareTrees(node1, node2) {
    if (!node1 || !node2) {
        return node1 == node2
    }
    if (node1.data !== node2.data) {
        return false
    }
    return compareTrees(node1.right, node2.right) && compareTrees(node1.left, node2.left)
}


const Tree1 = new BST()
const Tree2 = new BST()
const Tree3 = new BST()
const Tree4 = new BST()

const arr1 = [5, 1, 77, 32, 6, -11, 777]
const arr2 = [1, 77, 5, -11, 32, 6, 777]

for (let i = 0; i < arr1.length; i++) {
    let num = arr1[i]
    Tree1.insert(num)
    Tree2.insert(num)
    Tree3.insert(num)
}

for (let i = 0; i < arr2.length; i++) {
    let num = arr2[i]
    Tree4.insert(num)
}

console.log(compareTrees(Tree1.root, Tree2.root))
console.log(compareTrees(Tree2.root, Tree3.root))
console.log(compareTrees(Tree1.root, Tree4.root))
