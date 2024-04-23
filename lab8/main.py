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

    def insert_edge(self, vertex1, vertex2, edge=None):
        if (vertex1 in self.vertices()) and (vertex2 in self.vertices()):
            self.neighbours_list[vertex1][vertex2] = edge
            self.neighbours_list[vertex2][vertex1] = edge

    def delete_vertex(self, vertex):
        self.neighbours_list.pop(vertex)
        for v in self.vertices():
            self.neighbours_list[v].pop(vertex)

    def delete_edge(self, vertex1, vertex2):
        self.neighbours_list[vertex1].pop(vertex2)
        self.neighbours_list[vertex2].pop(vertex1)

    def neighbours(self, vertex_id):
        return self.neighbours_list[vertex_id].items()

    def vertices(self):
        return self.neighbours_list.keys()
    
class Vertex:
    def __init__(self, key, data=None):
        self.key = key
        self.data = data

    def __hash__(self):
        return hash(self.key)
    
    def __eq__(self, other):
        return self.key == other.key
        
    def __repr__(self):
        return "(" + str(self.key) + ", " + str(self.data) + ")"
    
graph = ListGraph()
A = Vertex("A")
B = Vertex("B")
C = Vertex("C")
graph.insert_vertex(A)
graph.insert_vertex(B)
graph.insert_edge(A, B)
graph.insert_edge(A, B, 2)
graph.insert_vertex(C)
graph.insert_edge(A, C)
print(graph.vertices())
# graph.delete_edge(A, B)
print(graph.neighbours_list)
