import sys
x = [1,2,3,4,5,6,7]
min_pos = 0
for i in range(len(x)):
	minm = sys.maxsize
	for j in range(min_pos,len(x)):
		if minm > x[j]:
			minm = x[j]
			pos = j
	x[min_pos],x[pos] = x[pos],x[min_pos]
	min_pos+=1
print(x)
