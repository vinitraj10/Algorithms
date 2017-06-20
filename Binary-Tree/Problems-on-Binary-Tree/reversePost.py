from ..package import BinaryTree

def preorder(root):
	if not root :
		return 
	stack=[]
	result=[]
	stack.append(root)
	while stack:
		node=stack.pop()
		result.append(node)
		if node.rightChild:
			stack.append(node.rightChild)
		if node.leftChild:
			stack.append(node.leftChild)
	result.reverse()
	print(" ".join(str(i) for i in result))

root=BinaryTree(1)
root.insertLeft(2)
root.insertLeft(4)
root.insertRight(3)
preorder(root)