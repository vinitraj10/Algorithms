'''
The Stock Span Problem
The stock span problem is a financial problem where we have a series of n daily price quotes for a stock and we need to calculate span of stock’s price for all n days. 
The span Si of the stock’s price on a given day i is defined as the maximum number of consecutive days just before the given day, for which the price of the stock on the current day is less than or equal to its price on the given day.
For example, if an array of 7 days prices is given as {100, 80, 60, 70, 60, 75, 85}, then the span values for corresponding 7 days are {1, 1, 1, 2, 1, 4, 6}


'''

stock=[int(x) for x in input().split()]
span=[0]*len(stock)
span[0]=1         # Since First stock don't have any previous stock to compare!! 
stack=[]
stack.append(0)   # Pushed the first index of the stock

for i in range(1,len(stock)):
	while len(stack) > 0 and stock[i] > stock[stack[-1]]:
		stack.pop()
	if len(stack) > 0:
		span[i]=i-stack[-1]
	else:
		span[i]=i
	stack.append(i)
print(span)