def search(x,p,q,n):
	if p<=q:
		m=len(x)
		mid=(p+q)//2
		if x[mid]== n:
			return mid
		elif x[mid]>n:
			return search(x,p,mid-1,n)
		else:
			return search(x,mid+1,q,n)
	return -1




print("Enter the List:-")
x=[int(x) for x in input().split()]
x.sort()
print("Enter the number to be searched :- ")
n=int(input())
ans=search(x,0,len(x)-1,n)
if ans == -1:
	print('Not Found')
else:
	print('Found at ',ans)