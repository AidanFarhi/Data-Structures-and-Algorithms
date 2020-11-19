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
        self.adj_list = []
        self.visited = False


# Approach with a stack data structure
# This will go down the right side of the tree first
def dfs_iterative(s_node):
    stack = [s_node]
    s_node.visited = True
    while stack:
        node = stack.pop()
        print(node.data)
        node.visited = True
        for n in node.adj_list:
            if not n.visited:
                stack.append(n)

# Recursive approach
# This will go down the left side of the tree first
def dfs_recursive(node):
    node.visited = True
    print(node.data)
    for n in node.adj_list:
        if not n.visited:
            dfs_recursive(n)

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

# Create connections
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

# dfs_iterative(node1)
# dfs_recursive(node1)
