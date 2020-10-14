"""
- BFS -

Applications:
- Visiting every node on a graph
- Dijkstra's algorithm does BFS if all the edge weights are 1

Running Time:
- O(V+E)

Memory:
- Not good

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
        self.predecessor = None


class BFS:
    def bfs(self, start_node):
        queue = []
        queue.append(start_node)
        start_node.visited = True
        while queue:
            node = queue.pop(0)
            print(f'Node data: {node.data}')
            for item in node.adj_list:
                if not item.visited:
                    item.visited = True
                    queue.append(item)


n1 = Node('A')
n2 = Node('B')
n3 = Node('C')
n4 = Node('D')
n5 = Node('E')

n1.adj_list.append(n2)
n1.adj_list.append(n3)
n2.adj_list.append(n4)
n4.adj_list.append(n5)

bfs = BFS()

bfs.bfs(n1)
