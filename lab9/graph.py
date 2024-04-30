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

    def insert_edge(self, vertex1, vertex2, edge=1):
        self.insert_vertex(vertex1)
        self.insert_vertex(vertex2)
        if vertex2 not in self.neighbours_list[vertex1] and vertex1 not in self.neighbours_list[vertex2]:
            self.neighbours_list[vertex1][vertex2] = edge
            self.neighbours_list[vertex2][vertex1] = edge

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