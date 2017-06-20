from package import BinaryTree
def FindSize(root):
	if not root:
		return 0
	return FindSize(root.leftChild)+FindSize(root.rightChild)+1

root=BinaryTree(1)
root.insertLeft(2)
root.insertLeft(4)
root.insertRight(3)
print(FindSize(root))