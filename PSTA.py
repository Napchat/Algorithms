"""Prim's Spanning Tree Algorithm

It belongs to a family of algorithms called the 'greedy algorithms'
"""

from PriorityQueue import PriorityQueue
from Graph import Graph
from Vertex import Vertex

def prim(G, start):
	pq = PriorityQueue()
	for v in G:
		v.setDistance(sys.maxsize)
		v.setPred(None)
	start.setDisatance(0)
	pq.build_heap([(v.getDistance(), v) for v in G])
	while not pq.is_empty():
		currentVert = pq.del_min()
		for nextVert in currentVert.getConnections():
			newCost = currentVert.getWeight(nextVert)
			if nextVert in pq and newCost < nextVert.getDistance():
				nextVert.setPred(currentVert)
				nextVert.setDisatance(newCost)
				pq.decrease_key(nextVert, newCost)