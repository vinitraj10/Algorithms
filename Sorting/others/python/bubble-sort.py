x = [4,1,45,23,0,5,3]
for i in range(len(x)):
	for j in range(len(x)-i-1):
		if x[j] > x[j+1]:
			x[j],x[j+1]=x[j+1],x[j]

print(x)