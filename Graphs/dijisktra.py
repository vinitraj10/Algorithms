import sys
class Graph:
	def __init__(self):
		self.adjlist = {}
	
	def add(self,nodeval):
		self.adjlist[nodeval]=[]

	def __str__(self):
		return str(self.adjlist)

#print("No of nodes please:-\n")
n = int(input())
graph = Graph()
sdt = {}
for i in range(n):
	#print("Enter name of node\n")
	node = input()
	graph.add(node)
	sdt[node] = sys.maxsize

for i in range(n):
	#print("Enter parent")
	val = input() # enter parent node
	#print("Enter neigbhour with weight")
	x = [x for x in input().split()] # list of neigbhour
	for i in range(0,len(x),2):
		graph.adjlist[val].append([x[i],int(x[i+1])]) # 1st index is node val and 2nd index is weight

q = []
print("Enter the source")
source = input() # Enter the source
sdt[source] = 0
q.append(source)
visited = set()

while(q):
	val = []
	for i in range(len(q)):
		val.append(sdt[q[i]])
	index = val.index(min(val))
	vertex = q.pop(index)
	visited.add(vertex)
	#print(vertex)
	nbr = graph.adjlist[vertex]
	#print(nbr)
	for i in range(0,len(nbr)):
		sdt[nbr[i][0]]=min(sdt[nbr[i][0]],nbr[i][1]+sdt[vertex])
		if nbr[i][0] not in visited:
			q.append(nbr[i][0])

print(sdt)