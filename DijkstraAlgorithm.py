from Graph import Graph
from Vertex import Vertex
from PriorityQueue import PriorityQueue

def dijkstra(aGraph, start):

    # Actually, it is a priority queue.
    pq = PriorityQueue()

    start.setDistance(0)

    # :meth:`biuld_heap` is O(logV)
    pq.build_heap([(v.getDistance(), v) for v in aGraph])
    while not pq.is_empty():

        # :meth:`del_min()` is O(logV), within the `while` loop, it is O(Vlog(V))
        currentVert = pq.del_min()

        # The `for` loop is O(E)
        for nextVert in currentVert.getConnections():
            newDist = currentVert.getDistance() + currentVert.getWeight(nextVert)
            if newDist < nextVert.getDistance():
                nextVert.setDistance(newDist)
                nextVert.setPred(currentVert)

                # :meth:`decrease_key` is within `for` loop, it is O(Elog(V))
                pq.decrease_key(nextVert, newDist)