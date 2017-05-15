
# A node With 3 parameters to implement a simple binary tree ,data to strore the value of Node and right left are the pointers to hold the address of there children nodes.
class Node:
	def __init__(self,data):
		self.data=data
		self.left=None
		self.right=None
class BinaryTree:
	def __init__(self):
		self.root=None

tree=BinaryTree()
tree.root=Node(1)
b=Node(2)
c=Node(3)
tree.root.left=b
tree.root.right=a
'''
This piece of code has created this tree:-
				1
			  /	  \
			 2     3
'''
