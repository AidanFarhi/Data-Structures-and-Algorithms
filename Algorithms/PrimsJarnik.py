"""
- Prim-Jarnik's Algorithm -

This algorithm will find the minimum spanning tree in a network
of nodes.

Prim-Jarnik's is a better algorithm for dense graphs (a lot of vertices)
and Kruskal's algorithm is better for sparse graphs (low number of vertices).

        - Running Time Complexity -
Best case: O(E*logE) | Worst Case: O(E*logV)

            - Memory Complexity -
                    O(E)
"""

import heapq


class Vertex:
    def __init__(self, data):
        self.data = data
        self.visited = False
        self.adj_list = []


class Edge:
    def __init__(self, weight, s_vertex, e_vertex):
        self.weight = weight
        self.s_vertex = s_vertex
        self.e_vertex = e_vertex

    def __lt__(self, other):
        return self.weight < other.weight


class PrimsJarnik:
    def __init__(self, unvisited_list):
        self.unvisited_list = unvisited_list
        self.spanning_tree = []
        self.edge_heap = []
        self.full_cost = 0

    def calculate_spanning_tree(self, vertex):
        self.unvisited_list.remove(vertex)
        while self.unvisited_list:
            for edge in vertex.adj_list:
                if edge.e_vertex in self.unvisited_list:
                    heapq.heappush(self.edge_heap, edge)
            min_edge = heapq.heappop(self.edge_heap)
            if min_edge.e_vertex in self.unvisited_list:
                self.spanning_tree.append(min_edge)
                print(f'Edge added to spanning tree: {min_edge.s_vertex.data}-{min_edge.e_vertex.data}')
                self.full_cost += min_edge.weight
                vertex = min_edge.e_vertex
                self.unvisited_list.remove(vertex)

    def get_spanning_tree(self):
        return self.spanning_tree

    def get_cost(self):
        return self.full_cost


vertexA = Vertex('A')
vertexB = Vertex('B')
vertexC = Vertex('C')
vertexD = Vertex('D')
vertexE = Vertex('E')
vertexF = Vertex('F')
vertexG = Vertex('G')

edgeAB = Edge(2, vertexA, vertexB)
edgeBA = Edge(2, vertexB, vertexA)
edgeAE = Edge(5, vertexA, vertexE)
edgeEA = Edge(5, vertexE, vertexA)
edgeAC = Edge(6, vertexA, vertexC)
edgeCA = Edge(6, vertexC, vertexA)
edgeAF = Edge(10, vertexA, vertexF)
edgeFA = Edge(10, vertexF, vertexA)
edgeBE = Edge(3, vertexB, vertexE)
edgeEB = Edge(3, vertexE, vertexB)
edgeBD = Edge(3, vertexB, vertexD)
edgeDB = Edge(3, vertexD, vertexB)
edgeCD = Edge(1, vertexC, vertexD)
edgeDC = Edge(1, vertexD, vertexC)
edgeCF = Edge(2, vertexC, vertexF)
edgeFC = Edge(2, vertexF, vertexC)
edgeDE = Edge(4, vertexD, vertexE)
edgeED = Edge(4, vertexE, vertexD)
edgeDG = Edge(5, vertexD, vertexG)
edgeGD = Edge(5, vertexG, vertexD)
edgeFG = Edge(3, vertexF, vertexG)
edgeGF = Edge(3, vertexG, vertexF)

unv_list = [
    vertexA, vertexB, vertexC, vertexD,
    vertexE, vertexF, vertexG
]

vertexA.adj_list.append(edgeAB)
vertexA.adj_list.append(edgeAC)
vertexA.adj_list.append(edgeAE)
vertexA.adj_list.append(edgeAF)
vertexB.adj_list.append(edgeBA)
vertexB.adj_list.append(edgeBD)
vertexB.adj_list.append(edgeBE)
vertexC.adj_list.append(edgeCA)
vertexC.adj_list.append(edgeCD)
vertexC.adj_list.append(edgeCF)
vertexD.adj_list.append(edgeDB)
vertexD.adj_list.append(edgeDC)
vertexD.adj_list.append(edgeDE)
vertexD.adj_list.append(edgeDG)
vertexE.adj_list.append(edgeEA)
vertexE.adj_list.append(edgeEB)
vertexE.adj_list.append(edgeED)
vertexF.adj_list.append(edgeFA)
vertexF.adj_list.append(edgeFC)
vertexF.adj_list.append(edgeFG)
vertexG.adj_list.append(edgeGD)
vertexG.adj_list.append(edgeGF)

prims_jarnik = PrimsJarnik(unv_list)
prims_jarnik.calculate_spanning_tree(vertexD)
print(prims_jarnik.get_cost())
