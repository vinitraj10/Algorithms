from package import BinaryTree
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


