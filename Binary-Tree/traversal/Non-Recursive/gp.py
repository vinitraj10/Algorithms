a,b,c=[int(x) for x in input().split()]
n=int(input())
k=0
m=(10**9)+7
A=[0]*n
B=[0]*n
A[0]=(a*c)%m
for i in range(1,n):
	A[i]=A[i-1]*((((a*b)%m)*c)%m) + A[i-1]*((a*b)%m) + A[i-1]*((a*c)%m)
	A[i]=A[i]%m
B[0]=(b*c)%m
for i in range(1,n):
	B[i]=B[i-1]*((((a*b)%m)*c)%m) + B[i-1]*((a*b)%m) + B[i-1]*((a*c)%m)
	B[i]=B[i]%m
	
m1=0
m2=1
n1=0
n2=1
for i in range(1,len(A)):
	if A[i]<A[m1]:
		m2=m1
		m1=i
for i in range(1,len(B)):
	if B[i]<B[n1]:
		n2=n1
		n1=i
if m1==n1:
	t1=(A[m1]+B[n2])%m
	t2=(A[m2]+B[n1])%m
	if t1 > t2:
		print(t2)
	else:
		print(t1)
else:
	total=A[m1]+B[n1]
	print(total%m)