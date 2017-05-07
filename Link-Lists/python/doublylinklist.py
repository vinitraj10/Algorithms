class Node:
	def __init__(self,value):
		self.value=value
		self.next=None
		self.prev=None



a=Node(1)
b=Node(2)
c=Node(3)

#doubly link list creation:-

'''a.next=b
b.prev=a
b.next=c
c.prev=b'''


#circular linklist
a.next=b
b.next=c
c.next=a

item =a
while True:
	print(item.value)
	item=item.next
	if item is a:
		print(item.value)
		break

#a->

