'''
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
'''

class Node:
    def __init__(self, data):
        self.data = data
        self.neighbors = []
        self.visited = False


# Recursive approach
def dfs(node):
    node.visited = True
    print(node.data)
    for n in node.neighbors:
        if not n.visited:
            dfs(n)


node1 = Node('A')
node2 = Node('B')
node3 = Node('C')
node4 = Node('D')
node5 = Node('E')

node1.neighbors.append(node2)
node1.neighbors.append(node3)
node2.neighbors.append(node4)
node4.neighbors.append(node5)

dfs(node1)
