"""
- Kruskal's Algorithm -

This algorithm will find the minimum spanning tree in a network
of nodes.

Applications:
- Finding minimum cost of adding a new power line to a network

- Running Time Complexity -
Worst Case: O(E logE)

"""


class Vertex:
    def __init__(self, data):
        self.data = data
        self.node = None


class Node:
    def __init__(self, height, node_id, parent):
        self.height = height
        self.node_id = node_id
        self.parent = parent


class Edge:
    def __init__(self, weight, s_vertex, e_vertex):
        self.weight = weight
        self.s_vertex = s_vertex
        self.e_vertex = e_vertex

    def __lt__(self, other):
        return self.weight < other.weight


class DisjointSet:
    def __init__(self, v_list):
        self.v_list = v_list
        self.root_nodes = []
        self.make_sets(v_list)

    def find(self, node):
        current = node
        while current.parent is not None:
            current = current.parent
        root = current
        current = node
        # Path compression
        while current is not root:
            temp = current.parent
            current.parent = root
            current = temp
        return root.node_id

    def merge(self, node1, node2):
        index1 = self.find(node1)
        index2 = self.find(node2)
        if index1 == index2:
            return
        root1 = self.root_nodes[index1]
        root2 = self.root_nodes[index2]
        if root1.height < root2.height:
            root1.parent = root2
            root2.height += 1
        elif root1.height > root2.height:
            root2.parent = root1
            root1.height += 1
        else:
            root2.parent = root1
            root1.height += 1

    def make_sets(self, v_list):
        for v in v_list:
            self.make_set(v)

    def make_set(self, vertex):
        node = Node(0, len(self.root_nodes), None)
        vertex.node = node
        self.root_nodes.append(node)


class KruskalAlgorithm:

    def spanning_tree(self, v_list, e_list):
        disjoint_set = DisjointSet(v_list)
        spanning_tree = []
        e_list.sort()
        for edge in e_list:
            s = edge.s_vertex
            e = edge.e_vertex
            if disjoint_set.find(s.node) is not disjoint_set.find(e.node):
                spanning_tree.append(edge)
                disjoint_set.merge(s.node, e.node)
        print('Minimum Spanning Tree is:')
        for edg in spanning_tree:
            print(edg.s_vertex.data + ' - ' + edg.e_vertex.data)


vertex1 = Vertex('A')
vertex2 = Vertex('B')
vertex3 = Vertex('C')
vertex4 = Vertex('D')
vertex5 = Vertex('E')
vertex6 = Vertex('F')
vertex7 = Vertex('G')

edge1 = Edge(2, vertex1, vertex2)
edge2 = Edge(6, vertex1, vertex3)
edge3 = Edge(5, vertex1, vertex5)
edge4 = Edge(10, vertex1, vertex6)
edge5 = Edge(3, vertex2, vertex4)
edge6 = Edge(3, vertex2, vertex5)
edge7 = Edge(1, vertex3, vertex4)
edge8 = Edge(2, vertex3, vertex6)
edge9 = Edge(4, vertex4, vertex5)
edge10 = Edge(5, vertex4, vertex7)
edge11 = Edge(5, vertex6, vertex7)

vertex_list = [
    vertex1, vertex2, vertex3, vertex4,
    vertex5, vertex6, vertex7
]

edge_list = [
    edge1, edge2, edge3, edge4, edge5, edge6,
    edge7, edge8, edge9, edge10, edge11
]

kruskal_algorithm = KruskalAlgorithm()
kruskal_algorithm.spanning_tree(vertex_list, edge_list)
