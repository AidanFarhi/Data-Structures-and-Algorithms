/*
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
*/

class Node {
    constructor(data, parent=null) {
        this.data = data
        this.parent = parent
        this.left = null
        this.right = null
        this.height = 0
    }
}

class AVL {
    constructor() {
        this.root = null
    }
    setHeight(node) {
        return Math.max(this.getHeight(node.left), this.getHeight(node.right)) + 1
    }
    getHeight(node) {
        if (node === null || node === undefined) return -1
        return node.height
    }
    getBalance(node) {
        return this.getHeight(node.left) - this.getHeight(node.right)
    }
    insert(data) {
        if (this.root === null) {
            this.root = new Node(data)
        } else {
            this.insertHelper(this.root, data)
        }
    }
    insertHelper(node, data) {
        if (node.data > data) {
            if (node.left) {
                this.insertHelper(node.left, data)
            } else {
                node.left = new Node(data, node)
                node.height = this.setHeight(node)
                this.handleViolation(node)
            }
        } else {
            if (node.right) {
                this.insertHelper(node.right, data)
            } else {
                node.right = new Node(data, node)
                node.height = this.setHeight(node)
                this.handleViolation(node)
            }
        }
    }
    handleViolation(node) {
        while (node) {
            node.height = this.setHeight(node)
            this.handleViolationHelper(node)
            node = node.parent
        }
    }
    handleViolationHelper(node) {
        let balance = this.getBalance(node)
        if (balance > 1) { // Left Heavy
            if (this.getBalance(node.left) < 0) { // Left Right Heavy
                this.rotateLeft(node.left)
            }
            this.rotateRight(node)
        }
        if (balance < -1) { // Right Heavy
            if (this.getBalance(node.right > 0)) { // Right Left Heavy
                this.rotateRight(node.right)
            }
            this.rotateLeft(node)
        }
    }
    remove(value) {
        if (this.root) {
            this.removeHelper(this.root, value)
        }
    }
    removeHelper(node, value) {
        if (node.data > value) {
            if (node.left) {
                this.removeHelper(node.left, value)
            }
        } else if (node.data < value) {
            if (node.right) {
                this.removeHelper(node.right, value)
            }
        } else {
            let parent = node.parent
            if (node.left === null && node.right === null) {
                if (parent) {
                    if (parent.left === node) {
                        parent.left = null
                    } else {
                        parent.right = null
                    }
                    this.handleViolation(parent)                    
                } else {
                    this.root = null
                }
            } else if (node.left && node.right === null) {
                if (parent) {
                    if (parent.left === node) {
                        parent.left = node.left
                        node.left.parent = parent
                    } else {
                        parent.right = node.left
                        node.left.parent = parent
                    }
                    this.handleViolation(parent)
                } else {
                    this.root = node.left
                    this.root.parent = null
                }
            } else if (node.left === null && node.right) {
                if (parent) {
                    if (parent.left === node) {
                        parent.left = node.right
                        node.right.parent = parent
                    } else {
                        parent.right = node.right
                        node.right.parent = parent
                    }
                    this.handleViolation(parent)
                } else {
                    this.root = node.right
                    this.root.parent = null
                }
            } else {
                let predecessor = this.getPredecessor(node.left)
                let tempData = predecessor.data
                predecessor.data = node.data
                node.data = tempData
                this.handleViolation(predecessor, value)
            }          
        }
    }
    getPredecessor(node) {
        if (node.right) {
            return this.getPredecessor(node.right)
        }
        return node
    }
    rotateLeft(node) {
        let tempRight = node.right
        let t = tempRight.left
        tempRight.left = node
        node.right = t
        if (t) {
            t.parent = node
        }
        let tempParent = node.parent
        node.parent = tempRight
        tempRight.parent = tempParent
        if (tempParent) {
            if (tempParent.left === node) {
                tempParent.left = tempRight
            }
            if (tempParent.right === node) {
                tempParent.right = tempRight
            }
        }
        if (node === this.root) {
            this.root = tempRight
        }
        node.height = this.setHeight(node)
        tempRight.height = this.setHeight(node)
    }
    rotateRight(node) {
        let tempLeft = node.left
        let t = tempLeft.right
        tempLeft.right = node
        node.left = t
        if (t) {
            t.parent = node
        }
        let tempParent = node.parent
        node.parent = tempLeft
        tempLeft.parent = tempParent
        if (tempParent) {
            if (tempParent.right === node) {
                tempParent.right = tempLeft
            }
            if (tempParent.left === node) {
                tempParent.left = tempLeft
            }
        }
        if (node === this.root) {
            this.root = tempLeft
        }
        node.height = this.setHeight(node)
        tempLeft.height = this.setHeight(tempLeft)
    }
    traverse() {
        if (this.root) {
            this.traverseHelper(this.root)
        }
    }
    traverseHelper(node) {
        if (node.left) {
            this.traverseHelper(node.left)
        }
        console.log(node.data)
        if (node.right) {
            this.traverseHelper(node.right)
        }
    }
    search(value) {
        if (this.root) {
            return this.searchHelper(this.root, value)
        }
    }
    searchHelper(node, value) {
        if (node.data > value) {
            if (node.left) {
                return this.searchHelper(node.left, value)
            } else {
                return false
            }
        } else if (node.data < value) {
            if (node.right) {
                return this.searchHelper(node.right, value)
            } else {
                return false
            }
        } else {
            if (node.data === value) return true
        }
    }
}

const avl = new AVL()
const arr = [1,2,3,4,5,-4,-77,-2, 34, 555]
for (let i = 0; i < arr.length; i++) {
    avl.insert(arr[i])
}
avl.traverse()
console.log('Root is:', avl.root.data)
console.log('Search for value 555:', avl.search(555))
console.log('Search for value 2:', avl.search(2))
console.log('Search for value 999:', avl.search(999))
