def binary_tree(root):
	return [root,[],[]]
def insertLeft(root,newBranch):
	t=root.pop(1)
	if len(t)>1:
		root.insert(1,[newBranch,t,[]])
	else:
		root.insert(1,[newBranch,[],[]])
	return root
def insertRight(root,newBranch):
	t=root.pop(2)
	if len(t)>1:
		root.insert(1,[newBranch,[],t])
	else:
		root.insert(1,[newBranch,[],[]])
	return root
def getRootVal(root):
	return root[0]
def setRootVal(root,newValue):
	root[0]=newValue
def getLeftChild(root):
	return root[1]
def getRightChild(root):
	return root[2]

r=binary_tree(3)
insertLeft(r,5)
insertLeft(r,4)
insertRight(r,2)
insertRight(r,8)

l=getLeftChild(r)
print('Left child is :- ',l)
right=getRightChild(r)
print('Right child is :- ',right) 
setRootVal(r,9)
print(r)
insertLeft(r,11)
print(r)
print(getRightChild(getRightChild(r)))

