class Node:
	def __init__(self,value):
		self.value=value
		self.next=None

def show(head):
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
show(x)