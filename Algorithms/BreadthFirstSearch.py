"""
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
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.adj_list = []
        self.visited = False


def bfs(start_node):
    queue = []
    queue.append(start_node)
    start_node.visited = True
    while queue:
        node = queue.pop(0)
        print(node.data)
        for n in node.adj_list:
            if not n.visited:
                n.visited = True
                queue.append(n)


# Initialize each node and add data
node1 = Node(100)
node2 = Node(200)
node3 = Node(300)
node4 = Node(400)
node5 = Node(500)
node6 = Node(600)
node7 = Node(700)
node8 = Node(800)
node9 = Node(900)
node10 = Node(1000)
node11 = Node(1100)
node12 = Node(1200)
node13 = Node(1300)
node14 = Node(1400)
node15 = Node(1500)
node16 = Node(1600)
node17 = Node(1700)

# Here we create connections between nodes
node1.adj_list.append(node2)
node1.adj_list.append(node3)
node1.adj_list.append(node4)
node2.adj_list.append(node5)
node2.adj_list.append(node6)
node2.adj_list.append(node7)
node3.adj_list.append(node8)
node4.adj_list.append(node9)
node5.adj_list.append(node10)
node5.adj_list.append(node11)
node8.adj_list.append(node12)
node8.adj_list.append(node13)
node9.adj_list.append(node14)
node9.adj_list.append(node15)
node15.adj_list.append(node16)
node15.adj_list.append(node17)

# Now run our BFS
# We should see data in ascending order from 100 -> 1700
bfs(node1)
