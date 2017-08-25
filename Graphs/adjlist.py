nodes = int(input())
edges = int(input())

adjlist=[]
for i in range(nodes+1):
	adjlist.append([])

for i in range(edges):
	x,y = [int(x) for x in input().split()]
	adjlist[x].append(y)

print(adjlist)
