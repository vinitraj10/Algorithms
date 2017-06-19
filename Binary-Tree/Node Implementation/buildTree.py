'''
Write a function buildTree that returns a tree using the list of lists functions that looks like this:
		
					a
				 /	   \
				b       c
				 \     / \
				  d    e  f

This is my solution for this question which you can find at http://interactivepython.org/runestone/static/pythonds/Trees/ListofListsRepresentation.html

'''
def buildTree(root):
	return [root,[],[]]

def insertLeft(root,newBranch):
	t=root.pop(1)
	if len(t)>1:
		root.insert(1,[newBranch,[t],[]])
	else:
		root.insert(1,[newBranch,[],[]])
	return root
def insertRight(root,newBranch):
	t=root.pop(2)
	if len(t)>1:
		root.insert(2,[newBranch,[],[t]])
	else:
		root.insert(2,[newBranch,[],[]])
	return root
def getLeftChild(root):
	return root[1]
def getRightChild(root):
	return root[2]

root=buildTree('a')
insertLeft(root,'b')
insertRight(root,'c')
getLeft=getLeftChild(root)
insertRight(getLeft,'d')
getRight=getRightChild(root)
insertLeft(getRight,'e')
insertRight(getRight,'f')
print(root)