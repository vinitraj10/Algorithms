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
Max=0
def Findmax(root):
	global Max
	if root is None:
		return Max
	if root.key >Max:
		Max=root.key
	Findmax(root.leftChild)
	Findmax(root.rightChild)
	return Max

root=BinaryTree(1)
root.insertLeft(2)
root.insertLeft(4)
root.insertRight(3)
print(Findmax(root))


