'''
- Dijkstra's Shortest Path Algorithm -

- Constructed in 1956 by Edsger Dijkstra.
- Handles positive edge weights (Not negative).
- It can find the shortest path from A to B, as
  well as constructing a shortest path tree: 
  Shortest path from a source to all other nodes.
- Asymptotically the fastest known single-source shortest-path
  algorithm for arbitrary directed graphs with unbounded 
  non-negative weights.
- Greedy algorithm.

Time Complexity: O(V*logV+E)
Data Structures Used: Heaps/Priority Queues

Shortest path problem:
Finding a path between two vertices in a graph such that the sum of
the weights of its edges in minimized.
'''
import sys
import heapq

class Edge:
    def __init__(self, weight, start_v, target_v):
        self.weight = weight
        self.start_v = start_v
        self.target_v = target_v


class Node:
    def __init__(self, data):
        self.data = data
        self.visited = False
        self.predecessor = None
        self.adj_list = []
        self.min_distance = sys.maxsize

    def __cpm__(self, other_v):
        return self.__cmp__(self.min_distance, other_v.mindistance)

    def __lt__(self, other_v):
        own_priority = self.min_distance
        other_priority = other_v.min_distance
        return own_priority < other_priority


class DSPA:
    def calc_shortest_path(self, vertex_list, start_vertex):
        q = []
        start_vertex.min_distance = 0
        heapq.heappush(q, start_vertex)
        while len(q) > 0:
            vertex = heapq.heappop(q)
            for edge in vertex.adj_list:
                u = edge.start_v
                v = edge.target_v
                new_distance = u.min_distance + edge.weight
                if new_distance < v.min_distance:
                    v.predecessor = u
                    v.min_distance = new_distance
                    heapq.heappush(q, v)
    
    def get_shortest_path_to(self, target_v):
        print(f'Shortest path to vertex {target_v.data} is: {target_v.min_distance}')
        node = target_v
        while node is not None:
            print(f'{node.data}')
            node = node.predecessor


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

algorithm = DSPA()
algorithm.calc_shortest_path(vertex_list, node1)
algorithm.get_shortest_path_to(node7)
