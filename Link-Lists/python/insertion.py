class Node:
	def __init__(self,data):
		self.data=data
		self.next=None

class LinkList:
	def __init__(self):
		self.head=None
	def show(self):
		item=self.head
		while item is not None:
			if item.next is not None:
				print(item.data,end='->')
			else:
				print(item.data)
			item=item.next
	def insertFront(self,val):
		item=Node(val)
		item.next=self.head
		self.head=item

'''def show(head):
	item=head
	while item is not None:
		if item.next is not None:
			print(item.value,end=' ->')
		else:
			print(item.value)
		item=item.next

def insert(head,d):
	n=int(input('Enter the no. to be inserted:-\n'))
	if d==1:
		item=Node(n)
		item.next=head
		head=item
		return head
	else:
		temp=Node(n)
		item=head
		for _ in range(d-2):
			item=item.next
		temp.next=item.next
		item.next=temp
		return head

N=int(input('Enter The intial Size of The list\n'))
print('Enter Head\n')
x=int(input())
p=Node(x)
item=p
print('Enter the list inputs now:-\n')
while N>1:
	k=int(input())
	q=Node(k)
	item.next=q
	q.next=None
	item=q
	N=N-1

print('Enter the Node No Where you want to insert:\n')
d=int(input())
x=insert(p,d) #Returns new head after deletion
show(x)'''

if __name__=='__main__':
	llist=LinkList()
	llist.head=Node(1)
	a=Node(2)
	b=Node(3)
	llist.head.next=a
	a.next=b
	llist.show()
	llist.insertFront(5)
	llist.show()
	llist.insertFront(6)
	llist.show()
	llist.insertFront(7)
	llist.show()
	llist.insertFront(8)
	llist.show()