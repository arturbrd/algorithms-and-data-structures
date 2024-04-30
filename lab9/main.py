from graf_mst import graf
from graph import ListGraph, Vertex
import numpy as np

def prim(graph: ListGraph):
    tree = ListGraph()
    vertices = graph.vertices()
    v = next(vertices)
    tree.insert_vertex(v)
    intree = {}
    distance = {}
    parent = {}
    for i in graph.vertices():
        intree[i] = 0
        distance[i] = np.float64('inf')
        parent[i] = None

    while intree[v] == 0:
        intree[v] = 1
        for n, dist in graph.neighbours(v):
            if dist < distance[n] and intree[n] == 0:
                distance[n] = dist
                parent[n] = v
        min_val = np.float64('inf')
        min_ver = None
        for i in graph.vertices():
            if intree[i] == 0 and distance[i] < min_val:
                min_val = distance[i]
                min_ver = i
        if min_ver is not None:
            tree.insert_vertex(min_ver)
            tree.insert_edge(parent[min_ver], min_ver, min_val)
            v = min_ver
    return tree

def printGraph(g):
    print("------GRAPH------")
    for v in g.vertices():
        print(v, end = " -> ")
        for (n, w) in g.neighbours(v):
            print(n, w, end=";")
        print()
    print("-------------------") 

def main():
    list_graph = ListGraph()

    for v1, v2, edge in graf:
        v1 = Vertex(v1)
        v2 = Vertex(v2)
        list_graph.insert_vertex(v1)
        list_graph.insert_vertex(v2)
        list_graph.insert_edge(v1, v2, edge)

    tree = prim(list_graph)

    printGraph(tree)

if __name__ == "__main__":
    main()
