/*
- Red Black Tree -
Rules:
1) Every node has a color either red or black.

2) Root of tree is always black.

3) There are no two adjacent red nodes (A red node cannot have a red parent or red child).

4) Every path from a node (including root) to any of its descendant NULL node has the same number of black nodes.

Same running time as AVL Trees
- Better for insertion operations than AVL trees but not as good for lookups
  because AVL trees are more rigidly balanced
*/

const Color = {
    red: 1, 
    black: 2
}

class Node {
    constructor(data, parent=null, color=Color.red) {
        this.data = data
        this.parent = parent
        this.color = color
        this.right = null
        this.left = null
    }
}

class RedBlackTree {
    constructor() {
        this.root = null
    }
    
    insert(data) {
        if (this.root === null) {
            this.root = new Node(data)
            this.handleViolation(this.root)
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
                this.handleViolation(node.left)
            }
        } else {
            if (node.right) {
                this.insertHelper(node.right, data)
            } else {
                node.right = new Node(data, node)
                this.handleViolation(node.right)
            }
        }
    }

    handleViolation(node) {
        while (node !== this.root && node.parent.color === Color.red) {
            let parent = node.parent
            let g_parent = parent.parent
            if (!g_parent) {
                return
            }
            if (g_parent.right === parent) {
                let uncle = g_parent.left
                if (uncle && uncle.color === Color.red) {
                    parent.color = Color.black
                    uncle.color = Color.black
                    g_parent.color = Color.red
                    node = g_parent
                } else {
                    if (node === parent.left) {
                        this.rotateRight(parent)
                        node = parent
                        parent = node.parent
                    }
                    g_parent.color = Color.red
                    parent.color = Color.black
                    this.rotateLeft(g_parent)
                }
            } else {
                let uncle = g_parent.right
                if (uncle && uncle.color === Color.red) {
                    parent.color = Color.black
                    uncle.color = Color.black
                    g_parent.color = Color.red
                    node = g_parent
                } else {
                    if (node === parent.right) {
                        this.rotateLeft(parent)
                        node = parent
                        parent = node.parent
                    }
                    g_parent.color = Color.red
                    parent.color = Color.black
                    this.rotateRight(g_parent)
                }
            }
        }
        if (this.root.color === Color.red) {
            this.root.color = Color.black
        }
    }
    
    rotateLeft(node) {
        let t_right = node.right
        let t = t_right.left
        t_right.left = node
        node.right = t
        if (t) {
            t.parent = node
        }
        let t_parent = node.parent
        node.parent = t_right
        t_right.parent = t_parent
        if (t_parent && t_parent.left === node) {
            t_parent.left = t_right
        }
        if (t_parent && t_parent.right === node) {
            t_parent.right = t_right
        }
        if (this.root === node) {
            this.root = t_right
        }
    }

    rotateRight(node) {
        let t_left = node.left
        let t = t_left.right
        t_left.right = node
        node.left = t
        if (t) {
            t.parent = node
        }
        let t_parent = node.parent
        node.parent = t_left
        t_left.parent = t_parent
        if (t_parent && t_parent.left === node) {
            t_parent.left = t_left
        } 
        if (t_parent && t_parent.right === node) {
            t_parent.right = t_left
        }
        if (node === this.root) {
            this.root = t_left
        }
    }

    traverse() {
        if (this.root) {
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
        let node = this.root
        while (node.right) {
            node = node.right
        }
        return node.data
    }

    getMin() {
        let node = this.root
        while (node.left) {
            node = node.left
        }
        return node.data
    }
}

const rbt = new RedBlackTree()

const testArray = [1,2,3,4,5,6,7,8,9,-1,-2,-3,-4,-5,-6]

for (let i = 0; i < testArray.length; i++) {
    rbt.insert(testArray[i])
}

rbt.traverse()
