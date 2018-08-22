x = [4,1,45,23,0,5,3]

for i in range(1,len(x)):
	val = x[i]
	pos = i
	while(pos>0 and a[pos-1]>val):
		a[pos] = a[pos-1]
		pos-=1
	a[pos] = val

print(x)