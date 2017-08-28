from Graph import Graph
from Vertex import Vertex

def knightGraph(bdSize):
    """Biuld the graph"""
    ktGraph = Graph()
    for row in range(bdSize):
        for col in range(bdSize):
            nodeId = posToNodeId(row, col, bdSize)
            newPositions = genLegalMoves(row, col, bdSize)
            for e in newPositions:
                nid = posToNodeId(e[0], e[1], bdSize)
                ktGraph.addEdge(nodeId, nid)
    return ktGraph

def posToNodeId(row, column, board_size):
    """Mark the Square"""
    return (row * board_size) + column

def genLegalMoves(x, y, bdSize):
    """Find the square you can move to"""
    newMoves = []
    moveOffsets = [(-1, -2), (-1, 2), (-2, -1), (-2, 1),
                   (1, -2), (1, 2), (2, -1), (2, 1)]
    for i in moveOffsets:
        newX = x + i[0]
        newY = y + i[1]
        if (legalCoord(newX, bdSize) and 
                legalCoord(newY, bdSize)):
            newMoves.append((newX, newY))
    return newMoves

def legalCoord(x, bdSize):
    """Check if you move out of board"""
    if x >= 0 and x < bdSize:
        return True
    else:
        return False

def knightTour(n, path, u, limit):
    """Depth first search

    Here the goal is to create the deepest depth first tree without any branches. The
    more general depth first search is actually easier. Its goal is to search as 
    deeply as possible, connecting as many nodes in the graph as possible and branching
    where necessary.

    Unvisited vertices are colored white, and visited vertices are colored gray.
    If all neighbors of a particular vertex have been explored and we have not 
    yet reached our goal length, we have reached a dead end. When we reach a dead
    end we must backtrack.

    Args:
        n: the current depth in the search tree.
        path: a list of vertices visited up to this point.
        u: the vertex in the graph we wish to explore.
        limit: the number of nodes in the path

    Returns:
        A bool variable that indicates if the square is a dead end
    `False` means it is a dead end.
    """
    u.setColor('gray')
    path.append(u)
    if n < (limit - 1):
        nbrList = orderByAvail(u)
        i = 0
        done = False
        while i < len(nbrList) and not done:
            if nbrList[i].getColor() == 'white':
                done = knightTour(n+1, path, nbrList[i], limit)
            i = i + 1

        # Prepare to backtrack
        if not done:
            path.pop()
            u.setColor('white')
    else:
        done = True
    return done

def orderByAvail(n):
    """Warnsdorff's algorithm
    
    It is a kind of heuristic algorithm.
    """
    resList = []
    for v in n.getConnections():
        if v.getColor() == 'white':
            c = 0   # the available moves of a square
            for w in v.getConnections():
                if w.getColor() == 'white':
                    c = c + 1
            resList.append((c, v))
    resList.sort(key=lambda x: x[0])
    return [y[1] for y in resList]

if __name__ == '__main__':
    g = knightGraph(8)
    print(g.numVertices)

    # Path is empty, so the depth is 0
    path = []
    u = g.vertList[44] # the start vertex

    knightTour(0, path, u, g.numVertices)
    print([x.id for x in g.vertList.values() if x.color == 'gray'])