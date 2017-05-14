class Node:
	def __init__(self,data):
		self.data=data
		self.next=None


class LinkedList:
	def __init__(self):
		self.head=None
	def show(self):
		item=self.head
		while item is not None:
			if item.next is None:
				print(item.data)
			else:
				print(item.data,end='->')
			item=item.next
	def delFirst(self):
		item=self.head
		self.head=item.next
	def delLast(self):
		item=self.head
		while item.next.next is not None:
			item=item.next
		item.next=None
	def delNode(self,n):
		item=self.head
		for i in range(n-2):
			item=item.next
		item.next=item.next.next


if __name__ == '__main__':
	llist=LinkedList()
	llist.head=Node(1)
	a=Node(2)
	b=Node(3)
	c=Node(4)
	d=Node(5)
	e=Node(6)
	f=Node(7)
	llist.head.next=a
	a.next=b
	b.next=c
	c.next=d
	d.next=e
	e.next=f
	llist.show()
	llist.delFirst()
	llist.show()
	llist.delLast()
	llist.show()
	llist.delNode(4)
	llist.show()
	llist.delNode(2)
	llist.show()	
	llist.delNode(3)
	llist.show()