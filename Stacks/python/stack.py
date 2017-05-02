class Stack:
	def __init__(self):
		self.items=[]
	def size(slef):
		return len(self.items)
	def push(self,item):
		return self.items.append(item)
	def pop(self):
		return self.items.pop()
	def isEmpty(self):
		return self.items == []
	def __str__(self):
		return str(self.items)


'''
s=Stack() # You can create stack like this
print(s.size()) # 0

s.push(6)
s.push(7)
s.push(8)
s.push('True')
s.push(9)
s.pop()
print(s.isEmpty) # False
print(s) # [6,7,8,True]
'''