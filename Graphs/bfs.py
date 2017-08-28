class Graph:
	def __init__(self,nodes,edges):
		self.graph=[]
		for i in range(nodes+1):
			self.graph.append([])

	def addEdge(self,v1,v2):
		self.graph[v1].append(v2)

	def bfs(self,s):
		visited = [False]*(len(self.graph))
		queue=[]
		queue.append(s)
		visited[s]=True
		
		while queue:
			s = queue.pop(0)
			print(s)

			for i in self.graph[s]:
				if visited[i] == False:
					queue.append(i)
					visited[i]=True

	def showGraph(self):
		print(self.graph)



g=Graph(4,5)
g.addEdge(1,2)
g.addEdge(1,3)
g.addEdge(1,4)
g.addEdge(3,4)
g.addEdge(4,2)
g.bfs(1)
#g.showGraph()

