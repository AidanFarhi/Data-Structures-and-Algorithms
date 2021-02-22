class Node {
    constructor(key, val) {
        this.key = key
        this.val = val
        this.left = null
        this.right = null
    }
}

class BST {
    constructor() {
        this.root = null
        this.size = 0
    }

    put(key, val) {
        this.root = this.putHelper(this.root, key, val)
    }

    putHelper(node, key, val) {
        if (node === null) {  // we have found an empty slot to put our node
            this.size++
            return new Node(key, val)
        } 
        else if (key < node.key) node.left = this.putHelper(node.left, key, val)
        else if (key > node.key) node.right = this.putHelper(node.right, key, val)
        else node.val = val  // key === node.key
        return node
    }

    get(key) {
        let node = this.root
        while (node !== null) {
            if (key < node.key) node = node.left
            else if (key > node.key) node = node.right
            else return node.val
        }
        return null  // if no match found
    }

    delete(key) {
        this.root = this.deleteHelper(this.root, key)
    }

    deleteHelper(node, key) {
        if (node === null) return null
        else if (key < node.key) node.left = this.deleteHelper(node.left, key)
        else if (key > node.key) node.right = this.deleteHelper(node.right, key)
        else { // found node to delete
            this.size--
            if (node.left === null) return node.right // case where node has no left child
            if (node.right === null) return node.left // case where node has no right child
            // case where node has two children
            let temp = node
            node = this.getMinOfSubtree(temp.right) // replace node with successor
            node.right = this.deleteMinOfSubtree(temp.right)
            node.left = temp.left
        }
        return node
    }

    getMinOfSubtree(node) {
        while (node.left !== null) node = node.left
        return node
    }

    deleteMinOfSubtree(node) {
        if (node.left === null) return node.right
        node.left = this.deleteMinOfSubtree(node.left)
        return node
    }

    getSize() {
        return this.size
    }

    getSortedKeys() {
        const arr = []
        this.getSortedKeysHelper(this.root, arr)
        return arr
    }

    getSortedKeysHelper(node, arr) {
        if (node === null) return
        if (node.left !== null) this.getSortedKeysHelper(node.left, arr)
        arr.push(node.key)
        this.getSortedKeysHelper(node.right, arr)
    }
}


function test() {

    const data = {
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

    const bst = new BST()
    
    for (let key in data) {
        bst.put(Number(key), data.key)
    }

    console.log(bst.getSize())

    bst.delete(90)
    bst.delete(1)

    console.log(bst.getSize())

    console.log(bst.getSortedKeys())
    console.log(bst.getSortedValues())
}


test()
