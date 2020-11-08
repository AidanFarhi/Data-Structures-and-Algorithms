/*
- Depth First Search -
This algorithms explores as far as possible along each
branch before back-tracking

This can be done either with recursion or with iteration.
If we use iteration, then we have to use a stack.

Time Complexity: O(V+E)

Memory Complexity: O(logN)

Applications: 
- Topological ordering
- Finding strongly connected components on a graph
- Detecting cycles
- Generating mazes or finding a way out of a maze
*/

class Node {
    constructor(data) {
        this.data = data
        this.neighbors = []
        this.visited = false
    }
}

function dfsRecursive(node) {
    node.visited = true
    console.log(node.data)
    for (let i = 0; i < node.neighbors.length; i++) {
        if (!node.neighbors[i].visited) {
            dfsRecursive(node.neighbors[i])
        }
    }
}

function dfsStack(start_node) {
    const stack = [start_node]
    while (stack) {
        let node = stack.pop()
        console.log(node.data)
        for (let i = 0; i < node.neighbors.length; i++) {
            if (!node.neighbors[i].visited) {
                node.neighbors[i].visited = true
                stack.push(node.neighbors[i])
            }
        }
    }
}

let node1 = new Node('A')
let node2 = new Node('B')
let node3 = new Node('C')
let node4 = new Node('D')
let node5 = new Node('E')

node1.neighbors.push(node2)
node1.neighbors.push(node3)
node2.neighbors.push(node4)
node4.neighbors.push(node5)
