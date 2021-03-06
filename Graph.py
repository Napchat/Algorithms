from Vertex import Vertex

class Graph(object):
    
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0

    def size(self):
        return self.numVertices

    def addVertex(self, key):
        self.numVertices = self.numVertices + 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        return newVertex
 
    def getVertex(self, key):
        if key in self.vertList:
            return self.vertList[key]
        return None

    def addEdge(self, f, t, cost=0):
        if f not in self.vertList:
            nv = self.addVertex(f)
        if t not in self.vertList:
            nv = self.addVertex(t)
        self.vertList[f].addNeighbor(self.vertList[t], cost)

    def delEdge(self, f, t):
        if f in self.vertList and t in self.vertList:
            if self.vertList[t] in self.vertList[f].getConnections():
                del self.vertList[f].connectedTo[self.vertList[t]]

    def __iter__(self):
        return iter(self.vertList.values())

    def __contains__(self, key):
        return key in self.vertList