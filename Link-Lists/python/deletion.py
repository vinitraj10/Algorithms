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

def delete(head,d):
	if d==1:
		item=head
		head=item.next
		return head
	elif d==N:
		item=head
		for i in range(n-1):
			item=item.next
		item.next=None
		return head
	else:
		item=head
		for i in range(1,d-1):
			item=item.next
		item.next=item.next.next
		return head


N=int(input('Enter The intial Size of The list\n'))
print('Enter Head\n')
x=int(input())
p=Node(x)
item=p
print('Enter the list inputs now:-')
while N>1:
	k=int(input())
	q=Node(k)
	item.next=q
	q.next=None
	item=q
	N=N-1

print('Enter the Node No you want to delete:\n')
d=int(input())
x=delete(p,d) #Returns new head after deletion
show(x)