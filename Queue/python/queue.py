class Queue:
	def __init__(self):
		self.items=[]
	def __str__(self):
		return str(self.items)
	def __getitem__(self,index):
		return self.items[index]
	def isEmpty(self):
		return self.items == []
	def enqueue(self,item):
		self.items.insert(0,item)    # so that the first input can be popped first
	def dequeue(self):
		return self.items.pop()
	def size(self):
		return len(self.items)




'''
#Here is the implementation:-


q=Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
print(q)
print(q.dequeue())
print(q.dequeue())
print(q.isEmpty())
print(q.size())
print(q)'''