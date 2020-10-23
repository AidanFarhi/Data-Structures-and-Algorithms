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
        this.neighbors = []
    }
}

function bfs(startNode) {
    const queue = [startNode]
    while (queue.length > 0) {
        let node = queue.shift()
        console.log(node.data)
        for (let n = 0; n < node.neighbors.length; n++) {
            if (!node.neighbors[n].visited) {
                node.neighbors[n].visited = true
                queue.push(node.neighbors[n])
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
node1.neighbors.push(node4)
node4.neighbors.push(node5)

bfs(node1)
