'''
Problem-link:https://www.hackerearth.com/practice/data-structures/stacks/basics-of-stacks/practice-problems/algorithm/signal-range/
Simmilar-to: https://www.hackerearth.com/practice/data-structures/stacks/basics-of-stacks/practice-problems/algorithm/monk-and-prisoner-of-azkaban/description/,
           https://www.hackerearth.com/practice/data-structures/arrays/1-d/practice-problems/algorithm/the-amazing-race-1/
This problem is based on stock-span problem,it is quite similar to it.
This is the solution of The Signaal Range hackerearth.com


'''



test=int(input())

for i in range(test):
    n=int(input())
    h=[int(h) for h in input().split()]
    r=[0]*n
    stack=[]
    r[0]=1
    stack.append(0)
    
    for i in range(1,n):
        while stack and h[stack[-1]]<=h[i]:
            stack.pop()
        if not stack:
            r[i]=i+1
        else:
            r[i]=i-stack[-1]
        stack.append(i)

    print(" ".join([str(i) for i in r]))


