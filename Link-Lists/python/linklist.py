class Node:
	def __init__(self,value):
		self.value=value
		self.nextnode=None



#Creating Nodes:-
a=Node(1)
b=Node(2)
c=Node(3)
#Now connecting those nodes by giving address of nextnode

a.nextnode=b
b.nextnode=c

'''
a->b->c->None



'''
print('Normal way to print')
print(a.value)
print(a.nextnode.value)
print(a.nextnode.nextnode.value)

print('------------------')

print('By using loop:-')

item=a
while item is not None:
	print(item.value,end=' ')
	item=item.nextnode