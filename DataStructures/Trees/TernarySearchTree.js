/* 
- Ternary Search Tree -

Every node has three children. left, middle, and right

Advantages:
- TST support sorting
- TST is better than hashing, especially for search misses
- Faster than hashmaps and more flexible than binary search trees
*/

class Node {
    constructor(char) {
        this.char = char
        this.left = null
        this.right = null
        this.middle = null
        this.value = null
    }
}

class TST {
    constructor() {
        this.root = null
    }

    insert(key, value) {
        this.root = this.insertHelper(this.root, key, value, 0)
    }

    insertHelper(node, key, value, index) {
        let ch = key[index]
        if (!node) {
            node = new Node(ch)
        }
        if (node.char > ch) {
            node.left = this.insertHelper(node.left, key, value, index)
        } else if (node.char < ch) {
            node.right = this.insertHelper(node.right, key, value, index)
        } else if (index < key.length - 1) {
            node.middle = this.insertHelper(node.middle, key, value, index + 1)
        } else {
            node.value = value
        }
        return node
    }

    get(key) {
        let node = this.getHelper(this.root, key, 0)
        return node ? node.value : null
    }

    getHelper(node, key, index) {
        let ch = key[index]
        if (!node) return null
        if (node.char > ch) {
            return this.getHelper(node.left, key, index)
        } else if (node.char < ch) {
            return this.getHelper(node.right, key, index)
        } else if (index < key.length - 1) {
            return this.getHelper(node.middle, key, index + 1)
        } else {
            return node
        }
    }
}

const tst = new TST()
tst.insert('hi', 100)
tst.insert('high', 200)
tst.insert('bye', 400)
tst.insert('goodbye', 900)

console.log(tst.get('hi'))
console.log(tst.get('high'))
console.log(tst.get('hig'))
console.log(tst.get('bye'))
console.log(tst.get('goodbye'))
console.log(tst.get('good'))