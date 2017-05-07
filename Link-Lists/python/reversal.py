def reverse(head):
	current=head
	nextnode=None
	prevnode=None

	while current:
		nextnode=current.next
		current.next=prevnode

		prevnode=current
		current=nextnode

	return prevnode

def show(head):
	item=head
	while item is not None:
		if item.next is not None:
			print(item.value,end='->')
		else:
			print(item.value)
		item=item.next

class Node:
	def __init__(self,value):
		self.value=value
		self.next=None


a=Node(1)
b=Node(2)
c=Node(3)
d=Node(4)


a.next=b
b.next=c
c.next=d

print('Linked List without reversal:-\n')
show(a)
print('---------------------------')
print('Linked List After Reversal:-\n')
x=reverse(a)
show(x)
