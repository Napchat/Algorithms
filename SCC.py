from Graph import Graph


def SCC(graph):
    pass

def graphTransposition(graph):
    for vertex in graph:
        for con in vertex.getConnections():
            g.addEdge(con, vertex)
            g.delEdge(vertex, con)

if __name__ == '__main__':
    g = Graph()
    g.addVertex('11')
    g.addVertex('13')
    g.addVertex('15')
    g.addEdge('11', '13')
    g.addEdge('13', '15')

    graphTransposition(g)

    v1 = g.getVertex('13')
    v2 = g.getVertex('15')

    for nb in v1.getConnections():
        print(nb.id)

    for nb in v2.getConnections():
        print(nb.id)