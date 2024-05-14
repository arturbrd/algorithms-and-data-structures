from graph import ListGraph, Vertex, printGraph, ford_fulkerson

def main():
    graph_0 = ListGraph()

    graf_0 = [ ('s','u',2), ('u','t',1), ('u','v',3), ('s','v',1), ('v','t',2)]

    graph_1 = ListGraph()

    graf_1 = [ ('s', 'a', 16), ('s', 'c', 13), ('a', 'c', 10), ('c', 'a', 4), ('a', 'b', 12), ('b', 'c', 9), ('b', 't', 20), ('c', 'd', 14), ('d', 'b', 7), ('d', 't', 4) ]

    graph_2 = ListGraph()

    graf_2 = [ ('s', 'a', 3), ('s', 'c', 3), ('a', 'b', 4), ('b', 's', 3), ('b', 'c', 1), ('b', 'd', 2), ('c', 'e', 6), ('c', 'd', 2), ('d', 't', 1), ('e', 't', 9)]

    for graph, graf in zip([graph_0, graph_1, graph_2], [graf_0, graf_1, graf_2]):
        for v1, v2, cap in graf:
            v1 = Vertex(v1)
            v2 = Vertex(v2)
            graph.insert_vertex(v1)
            graph.insert_vertex(v2)
            graph.insert_edge(v1, v2, cap)
            graph.insert_residual(v1, v2)

        print(ford_fulkerson(graph))
        printGraph(graph)
    

if __name__ == "__main__":
    main()

