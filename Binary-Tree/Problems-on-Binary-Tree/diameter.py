from package import BinaryTree

nodes,rootdata=[int(x) for x in input().split()]
root=BinaryTree(rootdata)
for i in range(nodes-1):
	path=input()
	path=list(path)
	ptr=root
	for j in range(len(path)):
		if path[j]=='L':
			if ptr.leftChild is None:
				ptr.leftChild=BinaryTree(0)
			ptr=ptr.leftChild
		else:
			if ptr.rightChild is None:
				ptr.rightChild=BinaryTree(0)
			ptr=ptr.rightChild
	ptr.key=int(input())

Max=0
def Diameter(root):
	global Max
	if not root :
		return 0
	left=Diameter(root.leftChild)
	right=Diameter(root.rightChild)
	if left+right > Max:
		Max=left+right
	return max(left,right)+1


print(Diameter(root))	