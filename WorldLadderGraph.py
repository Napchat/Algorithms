from Graph import Graph
from Vertex import Vertex
from Queue import Queue

def buildGraph(wordFile):
    d = {}
    g = Graph()
    with open(wordFile, 'r') as f:
        # Create buckets of words that differ by one letter
        for line in f:
            word = line[:-1]  # get rid of the '\n'
            for i in range(len(word)):
                bucket = word[:i] + '_' + word[i+1:]

                # If there are three words the same, that means the word belongs to that bucket;
                # or a new bucket should be created.
                if bucket in d:
                    d[bucket].append(word)
                else:
                    d[bucket] = [word]

        # Add vertices and edges for words in the same bucket
        for bucket in d.keys():
            for word1 in d[bucket]:
                for word2 in d[bucket]:
                    if word1 != word2:
                        g.addEdge(word1, word2)
    return g

def bfs(g, start):
    """Breadth First Search

    Searching a graph and adjusting the vertex states.

    Args:
        g: a gragh
        start: a starting vertex.

    Returns:
        None

    Raises:
        None
    """

    start.setDistance(0)
    start.setPred(None)
    vertQueue = Queue()
    vertQueue.enqueue(start)
    while vertQueue.size() > 0:
        currentVert = vertQueue.dequeue()
        for nbr in currentVert.getConnections():
            if nbr.getColor() == 'white':
                nbr.setColor('grey')
                nbr.setDistance(currentVert.getDistance() + 1)
                nbr.setPred(currentVert)
                vertQueue.enqueue(nbr)
        currentVert.setColor('black')

def traverse(y):
    while y.getPred():
        print(y.getId())
        y = y.getPred()
    print(y.getId())


if __name__ == '__main__':
    graph = buildGraph('wordfile.txt')
    start = graph.getVertex('fool')
    bfs(graph, start)
    traverse(graph.getVertex('sage'))