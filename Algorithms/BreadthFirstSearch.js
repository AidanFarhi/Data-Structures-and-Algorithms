/*
- BFS -

Applications:
- Visiting every node on a graph
- Dijkstra's algorithm does BFS if all the edge weights are 1

Running Time:
- O(V+E)

Memory:
- O(N)

Basics:
We use an empty Queue at the beginning and we keep checking whether we have visited
the given node or not. Keep iterating until the queue is empty.

Applications:
- Artificial Intellegence/Machine Learning. Robots can discover the surrounding more
  easily with BFS than DFS
- Important in maximum flow: Edmonds-Karp algorithm uses BFS for finding augmented paths
- Cheyen's algorithm in garbage collection -> it helps to maintain active references on the
  heap memory
- Serialization / Deserialization of a tree like structure (for example when order does matter)
  -> it allows the tree to be reconstructed in an effecient manner
*/

class Node {
    constructor(data) {
        this.data = data
        this.visited = false
        this.adjList = []
    }
}

function bfs(startNode) {
    const queue = [startNode]
    while (queue.length > 0) {
        let node = queue.shift()
        console.log(node.data)
        for (let n = 0; n < node.adjList.length; n++) {
            if (!node.adjList[n].visited) {
                node.adjList[n].visited = true
                queue.push(node.adjList[n])
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

// Now run our BFS
// We should see data in ascending order from 100 -> 1700
bfs(node1)
