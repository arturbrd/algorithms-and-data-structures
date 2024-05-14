import numpy as np

class ListGraph:
    def __init__(self):
        self.neighbours_list = {}

    def is_empty(self):
        if len(self.neighbours_list) == 0:
            return True
        else:
            return False

    def insert_vertex(self, vertex):
        if vertex not in self.neighbours_list:
            self.neighbours_list[vertex] = {}

    def insert_edge(self, vertex1, vertex2, capacity=1):
        self.insert_vertex(vertex1)
        self.insert_vertex(vertex2)
        if vertex2 not in self.neighbours_list[vertex1]:
            self.neighbours_list[vertex1][vertex2] = Edge(capacity, False)

    def insert_residual(self, vertex1, vertex2):
        self.insert_vertex(vertex1)
        self.insert_vertex(vertex2)
        if vertex1 not in self.neighbours_list[vertex2]:
            self.neighbours_list[vertex2][vertex1] = Edge(0, True)

    def delete_vertex(self, vertex):
        if vertex in self.neighbours_list:
            self.neighbours_list.pop(vertex)
        for v in self.vertices():
            if vertex in self.neighbours_list[v]:
                self.neighbours_list[v].pop(vertex)

    def delete_edge(self, vertex1, vertex2):
        if vertex2 in self.neighbours_list[vertex1]:
            self.neighbours_list[vertex1].pop(vertex2)
        if vertex1 in self.neighbours_list[vertex2]:
            self.neighbours_list[vertex2].pop(vertex1)

    def neighbours(self, vertex_id):
        return self.neighbours_list[vertex_id].items()

    def vertices(self):
        return iter(self.neighbours_list.keys())
    
    def get_vertex(self, vertex):
        return vertex
    
    def get_edge(self, vertex1, vertex2):
        if vertex1 in self.neighbours_list and vertex2 in self.neighbours_list[vertex1]:
            return self.neighbours_list[vertex1][vertex2]
    
    def bfs(self):
        visited = set()
        parent = {}
        queue = []
        s = Vertex('s')
        visited.add(s)
        queue.append(s)
        while len(queue) > 0:
            el = queue.pop(0)
            for key, edge in self.neighbours(el):
                if key not in visited and edge.residual > 0:
                    visited.add(key)
                    parent[key] = el
                    queue.append(key)
        return parent

class Vertex:
    def __init__(self, key, data=None):
        self.key = key
        self.data = data
        self.intree = 0
        self.distance = np.float64('inf')
        self.parent = None

    def __hash__(self):
        return hash(self.key)
    
    def __eq__(self, other):
        return self.key == other.key
        
    def __repr__(self):
        # return "(" + str(self.key) + ", " + str(self.data) + ")"
        return str(self.key)
    
class Edge:
    def __init__(self, capacity, isResidual):
        self.capacity = capacity 
        self.isResidual = isResidual
        if isResidual:
            self.residual = 0
            self.flow = 0 
            self.capacity = 0
        else:
            self.residual = capacity
            self.flow = 0
            self.capacity = capacity

    def __repr__(self):
        return str(self.capacity) + " " + str(self.flow) + " " + str(self.residual) + " " + str(self.isResidual)
    
def printGraph(g):
    print("------GRAPH------")
    for v in g.vertices():
        print(v, end = " -> ")
        for (n, w) in g.neighbours(v):
            print(n, w, end=";")
        print()
    print("-------------------") 

def path_analysis(graph, parent_dict):
    cur_vertex = Vertex('t')
    min_res = np.float64('inf')
    if cur_vertex not in parent_dict:
        return 0
    s = Vertex('s')
    while cur_vertex != s:
        cur_edge = graph.get_edge(parent_dict[cur_vertex], cur_vertex)
        if cur_edge.residual < min_res:
            min_res = cur_edge.residual
        cur_vertex = parent_dict[cur_vertex]
    return min_res

def path_aug(graph, parent_dict, min_res):
    cur_vertex = Vertex('t')
    if cur_vertex not in parent_dict:
        return 0
    s = Vertex('s')
    while cur_vertex != s:
        cur_edge = graph.get_edge(parent_dict[cur_vertex], cur_vertex)
        cur_edge_rev = graph.get_edge(cur_vertex, parent_dict[cur_vertex])
        if cur_edge.isResidual:
            cur_edge.residual -= min_res
            cur_edge_rev.flow -= min_res
            cur_edge_rev.residual += min_res
        else:
            cur_edge.flow += min_res
            cur_edge.residual -= min_res
            cur_edge_rev.residual += min_res
        cur_vertex = parent_dict[cur_vertex]

def ford_fulkerson(graph):
    parent_dict = graph.bfs()
    min_res = path_analysis(graph, parent_dict)
    while min_res > 0:
        path_aug(graph, parent_dict, min_res)
        parent_dict = graph.bfs()
        min_res = path_analysis(graph, parent_dict)
    sum = 0
    t = Vertex('t')
    for n, _ in graph.neighbours(t):
        rev_edge = graph.get_edge(n, t)
        if not rev_edge.isResidual:
            sum += rev_edge.flow
    return sum
