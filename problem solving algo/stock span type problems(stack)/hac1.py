'''
Problem-link: https://www.hackerearth.com/practice/data-structures/stacks/basics-of-stacks/practice-problems/algorithm/monk-and-prisoner-of-azkaban/description/
simmilar-to: https://www.hackerearth.com/practice/data-structures/arrays/1-d/practice-problems/algorithm/the-amazing-race-1/ ,
            https://www.hackerearth.com/practice/data-structures/stacks/basics-of-stacks/practice-problems/algorithm/signal-range/

This problem is based on stock-span problem,it is quite similar to it.
this is the solution of Monk and Prisoner of Azkaban from hackerearth.com
'''






n = int(input())
a = [int(x) for x in input().split()]
b=[0]*n
f=[0]*n
b[0]=-1
f[n-1]=-1
sb=[0]
fb=[n-1]
for i in range(1,n):
    while len(sb) > 0 and a[i]>=a[sb[-1]]:
        sb.pop()
    if len(sb)>0:
        b[i]=sb[-1]+1
    else:
        b[i]=-1
    sb.append(i)
#print(b)
for i in range(n-2,-1,-1):
    while len(fb)> 0 and a[i]>=a[fb[-1]]:
        fb.pop()
    if len(fb)>0:
        f[i]=fb[-1]+1
    else:
        f[i]=-1
    fb.append(i)
#print(f)
xsum=[0]*n
for i in range(0,n):
    xsum[i]=b[i]+f[i]

print(" ".join([str(i) for i in xsum]))