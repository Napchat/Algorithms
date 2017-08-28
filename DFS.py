from Graph import Graph

class DFSGraph(Graph):
	"""General depth first tree

	选一条路一直往下走，走不通了再回过去看分支有没有没探索过的路可以走

	:meth:`dfs` function and :meth:`dfvisit` function are going to 
	calculate the finish times of every vertices.
	"""

	def __init__(self):
		super().__init__()
		self.time = 0

	def dfs(self):
		for aVertex in self:
			aVertex.setColor('white')
			aVertex.setPred(-1)
		for aVertex in self:
			if aVertex.getColor() == 'white':
				self.dfsvisit(aVertex)

	def dfsvisit(self, startVertex):
		startVertex.setColor('gray')
		self.time += 1
		startVertex.setDiscovery(self.time)
		for nextVertex in startVertex.getConnections():
			if nextVertex.getColor() == 'white':
				nextVertex.setPred(startVertex)
				self.dfsvisit(nextVertex)
		startVertex.setColor('black')
		self.time += 1
		startVertex.setFinish(self.time)