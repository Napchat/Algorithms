from Graph import Graph
from Vertex import Vertex
from PriorityQueue import PriorityQueue

def dijkstra(aGraph, start):

	# Actually, it is a priority queue.
	pq = PriorityQueue()

	start.setDistance(0)
	pq.build_heap([(v.getDistance(), v) for v in aGraph])
	while not pq.is_empty():
		currentVert = pq.del_min()
		for nextVert in currentVert.getConnections():
			newDist = currentVert.getDistance() + currentVert.getWeight(nextVert)
			if newDist < nextVert.getDistance():
				nextVert.setDistance(newDist)
				nextVert.setPred(currentVert)
				pq.decrease_key(nextVert, newDist)