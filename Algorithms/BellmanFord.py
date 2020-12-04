"""
- Bellman-Ford Shortest Path algorithm -

Slower than Dijkstra's algorithm, but more robust because
it can handle negative edge weights as well

- Applications -
- On the FOREX market it can detect arbitrage situations

- Running Time Complexity -
    O(V * E)        
"""

import sys


class Node:

    def __init__(self, data):
        self.data = data
        self.min_distance = sys.maxsize
        self.predecessor = None
        self.visited = False


class Edge:

    def __init__(self, weight, s_vertex, e_vertex):
        self.weight = weight
        self.s_vertex = s_vertex
        self.e_vertex = e_vertex


class BellmanFord:

    HAS_CYCLE = False

    def calc_shortest_path(self, edge_list, vertex_list, start_vertex):
        start_vertex.min_distance = 0
        # Set new distances for all possible paths
        for i in range(len(vertex_list) - 1):  # V - 1 times
            for edge in edge_list:
                new_distance = edge.weight + edge.s_vertex.min_distance
                if new_distance < edge.e_vertex.min_distance:
                    edge.e_vertex.min_distance = new_distance
                    edge.e_vertex.predecessor = edge.s_vertex
        # Now check for a negative cycle
        for edge in edge_list:
            if self.has_negative_cycle(edge):
                self.HAS_CYCLE = True
                break

    def has_negative_cycle(self, edge):
        new_distance = edge.weight + edge.s_vertex.min_distance
        if new_distance < edge.e_vertex.min_distance:
            return True
        return False

    def shortest_path_to(self, vertex):
        if self.HAS_CYCLE:
            return 'Negative cycle detected, no possible solution.'
        else:
            show_path = ''
            node = vertex
            while node.predecessor is not None:
                show_path += node.data + ' '
                show_path += '-> '
                node = node.predecessor
            show_path += node.data
            return show_path


node1 = Node("A")
node2 = Node("B")
node3 = Node("C")
node4 = Node("D")
node5 = Node("E")
node6 = Node("F")
node7 = Node("G")
node8 = Node("H")

edge1 = Edge(5, node1, node2)
edge2 = Edge(8, node1, node8)
edge3 = Edge(9, node1, node5)
edge4 = Edge(15, node2, node4)
edge5 = Edge(12, node2, node3)
edge6 = Edge(4, node2, node8)
edge7 = Edge(7, node8, node3)
edge8 = Edge(6, node8, node6)
edge9 = Edge(5, node5, node8)
edge10 = Edge(4, node5, node6)
edge11 = Edge(20, node5, node7)
edge12 = Edge(1, node6, node3)
edge13 = Edge(13, node6, node7)
edge14 = Edge(3, node3, node4)
edge15 = Edge(11, node3, node7)
edge16 = Edge(9, node4, node7)

# Use these to test for a negative cycle
edge17 = Edge(1, node1, node2)
edge18 = Edge(1, node2, node3)
edge19 = Edge(-3, node3, node1)
neg_cycle_e_list = (edge17, edge18, edge19)

v_list = (node1, node2, node3, node4, node5, node6, node7, node8)
e_list = (
    edge1, edge2, edge3, edge4, edge5, edge6, edge7, edge8,
    edge9, edge10, edge11, edge12, edge13, edge14, edge15, edge16
)

bellman_ford = BellmanFord()
bellman_ford.calc_shortest_path(e_list, v_list, node1)
print(bellman_ford.shortest_path_to(node7))
