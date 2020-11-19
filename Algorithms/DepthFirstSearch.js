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
        this.adjList = []
        this.visited = false
    }
}

function dfsRecursive(node) {
    node.visited = true
    console.log(node.data)
    for (let i = 0; i < node.adjList.length; i++) {
        if (!node.adjList[i].visited) {
            dfsRecursive(node.adjList[i])
        }
    }
}

function dfsIterative(startNode) {
    const stack = [startNode]
    startNode.visited = true
    while (stack.length > 0) {
        let node = stack.pop()
        console.log(node.data)
        for (let i = 0; i < node.adjList.length; i++) {
            if (!node.adjList[i].visited) {
                node.adjList[i].visited = true
                stack.push(node.adjList[i])
            }
        }
    }
}

//Initialize each node and add data
const node1 = new Node(100)
const node2 = new Node(200)
const node3 = new Node(300)
const node4 = new Node(400)
const node5 = new Node(500)
const node6 = new Node(600)
const node7 = new Node(700)
const node8 = new Node(800)
const node9 = new Node(900)
const node10 = new Node(1000)
const node11 = new Node(1100)
const node12 = new Node(1200)
const node13 = new Node(1300)
const node14 = new Node(1400)
const node15 = new Node(1500)
const node16 = new Node(1600)
const node17 = new Node(1700)

//Here we create connections between nodes
node1.adjList.push(node2)
node1.adjList.push(node3)
node1.adjList.push(node4)
node2.adjList.push(node5)
node2.adjList.push(node6)
node2.adjList.push(node7)
node3.adjList.push(node8)
node4.adjList.push(node9)
node5.adjList.push(node10)
node5.adjList.push(node11)
node8.adjList.push(node12)
node8.adjList.push(node13)
node9.adjList.push(node14)
node9.adjList.push(node15)
node15.adjList.push(node16)
node15.adjList.push(node17)

// dfsRecursive(node1)
// dfsIterative(node1)
