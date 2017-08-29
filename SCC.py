import copy
from DFS import DFSGraph

class SCCGraph(DFSGraph):

    def __init__(self):
        super().__init__()

        # `SCCTree` saves the list of vertices of a component tree
        self.SCCTree = []

        # `SCCComponents` saves the list of strongly connected components of a graph
        self.SCCComponents = []

    def SCC_Components(self):
        # Calculate the finish times for each vertex
        self.dfs()

        # Compute the transposition of graph
        self.graphTransposition()

        # Get `SCCTree` and `SCCComponents`
        self.dfsSCC()

        # Print those components one by one
        for tree in self.SCCComponents:
            print(list(map(lambda x : x.id, tree)))

    def dfsSCC(self):
        for aVertex in self:
            aVertex.setColor('white')
            aVertex.setPred(-1)
        for aVertex in sorted(self, key=lambda x : x.finish_times, reverse=True):
            if aVertex.getColor() == 'white':
                self.SCCTree = []
                self.dfsvisitSCC(aVertex)
                self.SCCComponents.append(self.SCCTree)

    def dfsvisitSCC(self, startVertex):
        self.SCCTree.append(startVertex)
        startVertex.setColor('gray')
        self.time += 1
        startVertex.setDiscovery(self.time)
        for nextVertex in startVertex.getConnections():
            if nextVertex.getColor() == 'white':
                nextVertex.setPred(startVertex)
                self.dfsvisitSCC(nextVertex)
        startVertex.setColor('black')
        self.time += 1
        startVertex.setFinish(self.time)

    def graphTransposition(self):
        """Do a transposition of a graph"""

        # :meth:`deepcopy` is necessary, we need a dict the same as `graph.vertList` but has no
        # relationship with `graph.vertList`
        g = copy.deepcopy(self.vertList)
        for vertex in g.values():
            for con in vertex.getConnections():
                self.delEdge(vertex.id, con.id)
                self.addEdge(con.id, vertex.id)

if __name__ == '__main__':
    g = SCCGraph()
    g.addEdge('C', 'F')
    g.addEdge('F', 'H')
    g.addEdge('H', 'I')
    g.addEdge('I', 'F')
    g.SCC_Components()