class Queue:
	def __init__(self):
		self.items=[]
	def __str__(self):
		return str(self.items)
	def __getitem__(self,index):
		return self.items[index]
	def isEmpty(self):
		return self.items == []
	def enqueue(self,item):
		self.items.insert(0,item)    # so that the first input can be popped first
	def dequeue(self):
		return self.items.pop()
	def size(self):
		return len(self.items)

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