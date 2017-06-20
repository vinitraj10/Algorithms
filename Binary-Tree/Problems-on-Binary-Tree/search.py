from package import BinaryTree

def FindElement(root,data):
	if not root:
		return 0
	if root.key is data:
		return 1
	else:
		temp=FindElement(root.leftChild,data)
		if temp == 1:
			return 1
		else:
			return FindElement(root.rightChild,data)
'''
this 1 is the non recursive method for the following question

def Search(root,data):

	if not root:
		print("Not Found")
	stack=[]
	stack.append(root)
	while stack:
		node=stack.pop()
		if node.key is data:
			print("Found")
			flag=1
			break
		else:
			flag=0
		if node.rightChild:
			stack.append(node.rightChild)
		if node.leftChild:
			stack.append(node.leftChild)
	if flag is 0:
		print("Not Found!")'''

root=BinaryTree(1)
root.insertLeft(2)
root.insertLeft(4)
root.insertRight(3)
if FindElement(root,5) is 1:
	print("FOUND IN TREE") #It Will return 0 because it is not in the tree.
else:
	print("NOT FOUND")
