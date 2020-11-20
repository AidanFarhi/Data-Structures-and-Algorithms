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
        self.visited = False
        self.predecessor = None
        self.adj_list = []
        self.min_distance = sys.maxsize


class Edge:
    def __init__(self, weight, s_vertex, e_vertex):
        self.weight = weight
        self.s_vertex = s_vertex
        self.e_vertex = e_vertex


class BellmanFord:

    HAS_CYCLE = False

    def calc_shortest_path_from(self, v_list, e_list, s_vertex):
        s_vertex.min_distance = 0
        for i in range(len(v_list) - 1):
            for edge in e_list:
                s = edge.s_vertex
                e = edge.e_vertex
                new_distance = s.min_distance + edge.weight
                if new_distance < e.min_distance:
                    e.min_distance = new_distance
                    e.predecessor = s

        for edge in e_list:
            if self.has_cycle(edge):
                print('Negative cycle detected...')
                BellmanFord.HAS_CYCLE = True
                return

    def has_cycle(self, edge):
        if (edge.s_vertex.min_distance + edge.weight) < edge.e_vertex.min_distance:
            return True
        else:
            return False

    def get_shortest_path_to(self, target_vertex):
        if not BellmanFord.HAS_CYCLE:
            print('Shortest path exists with distance:', target_vertex.min_distance)
            print('Shortest path to:', target_vertex.data)
            node = target_vertex
            while node is not None:
                print(node.data)
                node = node.predecessor
        else:
            print('Negative cycle detected.')


node1 = Node('A')
node2 = Node('B')
node3 = Node('C')
node4 = Node('D')
node5 = Node('E')
node6 = Node('F')
node7 = Node('G')
node8 = Node('H')

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

node1.adj_list.append(edge1)
node1.adj_list.append(edge2)
node1.adj_list.append(edge3)
node2.adj_list.append(edge4)
node2.adj_list.append(edge5)
node2.adj_list.append(edge6)
node8.adj_list.append(edge7)
node8.adj_list.append(edge8)
node5.adj_list.append(edge9)
node5.adj_list.append(edge10)
node5.adj_list.append(edge11)
node6.adj_list.append(edge12)
node6.adj_list.append(edge13)
node3.adj_list.append(edge14)
node3.adj_list.append(edge15)
node4.adj_list.append(edge16)

vertex_list = (node1, node2, node3, node4, node5, node6, node7, node8)
edge_list = (
    edge1, edge2, edge3, edge4, edge5, edge6, edge7, edge8,
    edge9, edge10, edge11, edge12, edge13, edge14, edge15, edge16
)

bf = BellmanFord()
bf.calc_shortest_path_from(vertex_list, edge_list, node1)
# This should print A -> E -> F -> C -> G
bf.get_shortest_path_to(node7)