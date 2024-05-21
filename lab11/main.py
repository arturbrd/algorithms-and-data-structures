import copy

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

class Matrix:
    def __init__(self, mtrx, val=0):
        if isinstance(mtrx, tuple):
            self.__mtrx = []
            for i in range(mtrx[0]):
                self.__mtrx.append([val for x in range(mtrx[1])])
        else:
            self.__mtrx = mtrx

        for r in range(len(self.__mtrx)):
            for c in range(len(self.__mtrx[r])):
                if self.__mtrx[r][c] == None:
                    self.__mtrx[r][c] = 0

    def __add__(self, other):
        if self.size() != other.size():
            return None
        
        new = []
        for si, oi in zip(self.__mtrx, other):
            inner = []
            for sj, oj in zip(si, oi):
                inner.append(sj+oj)
            new.append(inner)

        return Matrix(new)

    def __mul__(self, other):
        nrows, s_cols = self.size()
        o_rows, ncols = other.size()
        if s_cols != o_rows:
            return None

        new_table = []
        for i in range(nrows):
            new_row = []
            for j in range(ncols):
                sum = 0
                for k in range(s_cols):
                    sum += self[i][k]*other[k][j]
                new_row.append(sum)
            new_table.append(new_row)

        return Matrix(new_table)

    def __getitem__(self, i):
        return self.__mtrx[i]
    
    def __str__(self):
        mtrx_str = ""
        for i in self.__mtrx:
            line = "|"
            for j in i:
                if j >= 0:
                    line += " "
                line = line+str(j)+"  "
            line = line[:-1]
            line += "|\n"
            mtrx_str += line
        mtrx_str = mtrx_str[:-1]
        return mtrx_str

    def size(self):
        return len(self.__mtrx), len(self.__mtrx[0])
    
    def __eq__(self, other):
        for s_row, o_row in zip(self, other):
            if s_row != o_row:
                return False
        return True

def transpose(mtrx):
    rows, cols = mtrx.size()
    new_table = []
    for i in range(cols):
        new_line = []
        for j in range(rows):
            new_line.append(mtrx[j][i])
        new_table.append(new_line)
    return Matrix(new_table)

def printGraph(g):
    print("------GRAPH------")
    for v in g.vertices():
        print(v, end = " -> ")
        for (n, w) in g.neighbours(v):
            print(n, w, end=";")
        print()
    print("-------------------") 

def ullmann(used, M_mtrx, G_mtrx, P_mtrx, izomorphs, num_of_calls = 0, cur_row = 0):
    num_of_calls += 1
    if cur_row == M_mtrx.size()[0]:
        if M_mtrx*transpose(M_mtrx*G_mtrx) == P_mtrx: 
           izomorphs.append(copy.deepcopy(M_mtrx))
        return num_of_calls
    for c in range(M_mtrx.size()[1]):
        if not used[c]:
            used[c] = True
            for i in range(M_mtrx.size()[1]):
                M_mtrx[cur_row][i] = 0
            M_mtrx[cur_row][c] = 1
            num_of_calls = ullmann(used, M_mtrx, G_mtrx, P_mtrx, izomorphs, num_of_calls, cur_row+1)
            used[c] = False
    return num_of_calls

def ullmann2(used, M_mtrx, G_mtrx, P_mtrx, izomorphs, num_of_calls = 0, cur_row = 0):
    num_of_calls += 1
    if cur_row == M_mtrx.size()[0]:
        if M_mtrx*transpose(M_mtrx*G_mtrx) == P_mtrx: 
           izomorphs.append(copy.deepcopy(M_mtrx))
        return num_of_calls
    M_mtrx_copy = copy.deepcopy(M_mtrx)
    for c in range(M_mtrx.size()[1]):
        if not used[c] and M_mtrx[cur_row][c] != 0:
            used[c] = True
            for i in range(M_mtrx.size()[1]):
                M_mtrx_copy[cur_row][i] = 0
            M_mtrx_copy[cur_row][c] = 1
            num_of_calls = ullmann2(used, M_mtrx_copy, G_mtrx, P_mtrx, izomorphs, num_of_calls, cur_row+1)
            used[c] = False
    return num_of_calls

def ullmann3(used, M_mtrx, G_mtrx, P_mtrx, izomorphs, num_of_calls = 0, cur_row = 0):
    num_of_calls += 1
    if cur_row == M_mtrx.size()[0]:
        if M_mtrx*transpose(M_mtrx*G_mtrx) == P_mtrx: 
           izomorphs.append(copy.deepcopy(M_mtrx))
        return num_of_calls
    M_mtrx_copy = copy.deepcopy(M_mtrx)
    prune(M_mtrx_copy, P_mtrx, G_mtrx)
    for c in range(M_mtrx.size()[1]):
        if not used[c] and M_mtrx[cur_row][c] != 0:
            used[c] = True
            for i in range(M_mtrx.size()[1]):
                M_mtrx_copy[cur_row][i] = 0
            M_mtrx_copy[cur_row][c] = 1
            num_of_calls = ullmann3(used, M_mtrx_copy, G_mtrx, P_mtrx, izomorphs, num_of_calls, cur_row+1)
            used[c] = False
    return num_of_calls

def prune(M, P, G):
    while True:
        changed = False
        for i in range(M.size()[0]):
            for j in range(M.size()[1]):
                if M[i][j] == 1:
                    to_break = False
                    for x in range(len(P[i])):
                        if P[i][x] == 0:
                            continue
                        for y in range(len(G[j])):
                            if G[j][y] == 1 and M[x][y] == 1:
                                to_break = True
                                break
                        if to_break:
                            break
                    else:
                        M[i][j] = 0
                        changed = True
        if not changed:
            break

def main():
    graph_G_tab = [ ('A','B',1), ('B','F',1), ('B','C',1), ('C','D',1), ('C','E',1), ('D','E',1)]
    graph_P_tab = [ ('A','B',1), ('B','C',1), ('A','C',1)]

    graph_G = MatrixGraph()
    for v1, v2, e in graph_G_tab:
        graph_G.insert_vertex(v1)
        graph_G.insert_vertex(v2)
        graph_G.insert_edge(v1, v2, e)
    graph_P = MatrixGraph()
    for v1, v2, e in graph_P_tab:
        graph_P.insert_vertex(v1)
        graph_P.insert_vertex(v2)
        graph_P.insert_edge(v1, v2, e)
    mtrx = [[0 for _ in range(len(graph_G.mtrx))] for _ in range(len(graph_P.mtrx))]
    M = Matrix(copy.deepcopy(mtrx))
    P = Matrix(graph_P.mtrx)
    G = Matrix(graph_G.mtrx)

    izomorphs = []
    num_of_calls = ullmann([False for _ in range(M.size()[1])], M, G, P, izomorphs)
    print(len(izomorphs), num_of_calls)

    M0 = copy.deepcopy(mtrx)
    for i in range(len(graph_P.mtrx)):
        for j in range(len(graph_G.mtrx)):
            if graph_P.mtrx[i].count(1) <= graph_G.mtrx[j].count(1):
                M0[i][j] = 1
    M0 = Matrix(M0)
    M0_2 = copy.deepcopy(M0)
    izomorphs = []
    num_of_calls = ullmann2([False for _ in range(M.size()[1])], M0, G, P, izomorphs)
    print(len(izomorphs), num_of_calls)

    izomorphs = []
    num_of_calls = ullmann3([False for _ in range(M.size()[1])], M0_2, G, P, izomorphs)
    print(len(izomorphs), num_of_calls)


if __name__ == "__main__":
    main()
