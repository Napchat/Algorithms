class Vertex(object):
    
    def __init__(self, key):
        self.id = key
        self.connectedTo = {}
        self.distance = 0
        self.predecessor = None
        self.color = 'white'

        # `discovery_times` and `finish_times` are used in DFS.

        # The discovery time tracks the number of steps in the algorithm
        # before a vertex if first encountered.
        self.discovery_times = None

        # The finish time is the number of steps in the algorithm before a
        # vertex is colored black.
        self.finish_times = None

    def addNeighbor(self, nbr, weight=0):
        self.connectedTo[nbr] = weight

    def getConnections(self):
        """Get the connected vertex.

        Returns:
            Vertex instances which are connected by the caller.
        """
        return list(self.connectedTo.keys())

    def getId(self):
        return self.id

    def getWeight(self, nbr):
        return self.connectedTo[nbr]

    def setDistance(self, n):
        self.distance = n

    def getDistance(self):
        return self.distance

    def setPred(self, pred):
        self.predecessor = pred

    def getPred(self):
        return self.predecessor

    def setColor(self, color):
        self.color = color

    def getColor(self):
        return self.color

    def setDiscovery(self, time):
        self.discovery_times = time

    def setFinish(self, time):
        self.finish_times = time

    def getFinish(self):
        return self.finish_times

    '''def __str__(self):
        """当调用str(self)时的值"""
        return str(self.id) + 'connectedTo: ' + str([x.id for x in self.connectedTo])'''

if __name__ == '__main__':
    v1 = Vertex('BeiJing')
    v2 = Vertex('NanJing')
    v3 = Vertex('ChongQing')

    v1.addNeighbor(v2, 4)
    v1.addNeighbor(v3, 12)

    print('\n' + str(v1) + '\n')
    print(v1.getConnections())
