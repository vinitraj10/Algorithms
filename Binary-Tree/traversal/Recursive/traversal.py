class BinaryTree:
	def __init__(self,root):
		self.key=root
		self.leftChild=None
		self.rightChild=None
	def insertLeft(self,root):
		if self.leftChild==None:
			self.leftChild=BinaryTree(root)
		else:
			tempNode=BinaryTree(root)
			tempNode.leftChild=self.leftChild
			self.leftChild=tempNode
	def insertRight(self,root):
		if self.rightChild==None:
			self.rightChild=BinaryTree(root)
		else:
			tempNode=BinaryTree(root)
			tempNode.rightChild=self.rightChild
			self.rightChild=tempNode
	def getRightChild(self):
		return self.rightChild
	def getLeftChild(self):
		return self.leftChild
	def getRootVal(self):
		return self.key
	def setRootVal(self,root):
		self.key=root
	def __str__(self):
		return str(self.key)

def Preorder(root):
	if not root:
		return
	print(root.key,end=" ")
	Preorder(root.leftChild)
	Preorder(root.rightChild)
def Inorder(root):
	if not root:
		return 
	Inorder(root.leftChild)
	print(root.key,end=" ")
	Inorder(root.rightChild)
def Postorder(root):
	if not root:
		return
	Postorder(root.leftChild)
	Postorder(root.rightChild)
	print(root.key,end=" ")
root=BinaryTree(1)
root.insertLeft(2)
root.insertLeft(4)
root.insertRight(3)
root.insertRight(5)
print("\nPre-order traversal of the tree is :-\n")
Preorder(root)
print("\nInorder taversal of the tree is:-\n")
Inorder(root)
print("\nPost-order traversal of the tree is :-\n")
Postorder(root)