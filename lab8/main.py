import polska

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
        return self.neighbours_list.keys()
    
    def get_vertex(self, vertex):
        return vertex

class MatrixGraph:
    def __init__(self):
        self.mtrx = []
        self.vertices_tab = []

    def is_empty(self):
        if len(self.vertices_tab) == 0:
            return True
        else:
            return False

    def insert_vertex(self, vertex):
        if vertex not in self.vertices_tab:
            self.vertices_tab.append(vertex)
            for row in self.mtrx:
                row.append(None)
            self.mtrx.append([None for _ in range(len(self.vertices_tab))])

    def insert_edge(self, vertex1, vertex2, edge=1):
        self.insert_vertex(vertex1)
        self.insert_vertex(vertex2)
        v1_id = self.get_vertex_id(vertex1)
        v2_id = self.get_vertex_id(vertex2)
        if self.mtrx[v1_id][v2_id] == None and self.mtrx[v2_id][v1_id] == None:
            self.mtrx[v1_id][v2_id] = edge
            self.mtrx[v2_id][v1_id] = edge

    def delete_vertex(self, vertex):
        v_id = self.get_vertex_id(vertex)
        if v_id is not None:
            self.mtrx.pop(v_id)
            for i in self.mtrx:
                i.pop(v_id)
            self.vertices_tab.pop(v_id)

    def delete_edge(self, vertex1, vertex2):
        v1_id = self.get_vertex_id(vertex1)
        v2_id = self.get_vertex_id(vertex2)
        if v1_id is not None and v2_id is not None:
            self.mtrx[v1_id][v2_id] = None
            self.mtrx[v2_id][v1_id] = None

    def neighbours(self, vertex_id):
        val = None
        for i in self.vertices():
            if self.mtrx[vertex_id][i] is not None:
                yield i, self.mtrx[vertex_id][i]

    def vertices(self):
        val = 0
        while val < len(self.vertices_tab):
            yield val
            val += 1
    
    def get_vertex(self, vertex_id):
        return self.vertices_tab[vertex_id]
    
    def get_vertex_id(self, vertex):
        for i in self.vertices():
            if vertex == self.vertices_tab[i]:
                return i
        return None

class Vertex:
    def __init__(self, key, data=None):
        self.key = key
        self.data = data

    def __hash__(self):
        return hash(self.key)
    
    def __eq__(self, other):
        return self.key == other.key
        
    def __repr__(self):
        # return "(" + str(self.key) + ", " + str(self.data) + ")"
        return str(self.key)
    
def test_graph(graph):
    graph.insert_vertex(Vertex('K'))

    for v1, v2 in polska.graf:
        v1 = Vertex(v1)
        v2 = Vertex(v2)
        graph.insert_vertex(v1)
        graph.insert_vertex(v2)
        graph.insert_edge(v1, v2)

    graph.delete_vertex(Vertex('K'))

    graph.delete_edge(Vertex('W'), Vertex('E'))
    polska.draw_map(graph)

def main():
    list_graph = ListGraph()
    mtrx_graph = MatrixGraph()

    test_graph(list_graph)
    # test_graph(mtrx_graph)

if __name__ == "__main__":
    main()

