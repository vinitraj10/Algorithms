class Graph:
	def __init__(self,nodes,edges):
		self.graph=[]
		for i in range(nodes+1):
			self.graph.append([])
		self.visited=[False]*(len(self.graph))

	def addEdge(self,v1,v2):
		self.graph[v1].append(v2)

	def dfs(self,source):
		self.visited[source]=True
		print(source)
		for i in self.graph[source]:
			if not self.visited[i]:
				self.dfs(i)
	def dfs_stack(self,source):
		stack=[]
		stack.append(source)
		self.visited[source] = True
		while stack:
			top=stack.pop()
			print(top)
			for i in self.graph[top]:
				if not self.visited[i]:
					stack.append(i)
					self.visited[i]=True




g=Graph(4,5)
g.addEdge(1,2)
g.addEdge(1,3)
g.addEdge(1,4)
g.addEdge(3,4)
g.addEdge(4,2)
g.dfs_stack(1)