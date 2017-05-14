class Node:
	def __init__(self,data):
		self.data=data
		self.next=None

class LinkedList:
	def __init__(self):
		self.head=None
	def printlist(self):
		item=self.head
		while item is not None:
			if item.next is None:
				print(item.data)
			else:
				print(item.data,end='->')
			item=item.next


llist=LinkedList()
llist.head=Node(1)
a=Node(2)
b=Node(3)
llist.head.next=a
a.next=b

if __name__=='__main__':
	llist.printlist()
