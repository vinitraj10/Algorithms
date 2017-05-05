class Stack:
    def __init__(self):
        self.items=[]
    def size(self):
        return len(self.items)
    def push(self,item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def isEmpty(self):
        return self.items == []
    def __str__(self):
        return str(self.items)
    def __getitem__(self,index):
        return self.items[index] 


def balanceCheck(symbol):
    index=0
    balanced=True
    s=Stack()
    while index <len(symbol) and balanced:
        item=symbol[index]
        if item == '(' or item == '[' or item == '{':
            s.push(item)
        else:
            if s.isEmpty():
                balanced=False
            else:
                s.pop()
        
        index=index+1

    if  balanced and s.isEmpty():
        return True
    else:
        return False


print(balanceCheck('({[]})'))
print(balanceCheck('({([{{{((((()))))}}}])})'))
print(balanceCheck('([)({})])[[[[[['))