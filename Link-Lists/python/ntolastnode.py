class Node:
	def __init__(self,value):
		self.value=value
		self.next=None

def ntolastnode(head):
	item=head
	count=0
	while item is not None:
		item=item.next
		count=count+1
	p=head
	for i in range(count-n):
		p=p.next
	return p
a=Node(1)
b=Node(2)
c=Node(3)
d=Node(4)
a.next=b
b.next=c
c.next=d
n = int(input('Enter the value of n which value you want to return from last node:-\n'))
answer=ntolastnode(a)
print(answer.value)