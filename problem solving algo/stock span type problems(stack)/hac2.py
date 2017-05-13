'''
Problem-link: https://www.hackerearth.com/practice/data-structures/arrays/1-d/practice-problems/algorithm/the-amazing-race-1/
Simmilar-to: https://www.hackerearth.com/practice/data-structures/stacks/basics-of-stacks/practice-problems/algorithm/monk-and-prisoner-of-azkaban/description/,
            https://www.hackerearth.com/practice/data-structures/stacks/basics-of-stacks/practice-problems/algorithm/signal-range/

This problem is based on stock-span problem,it is quite similar to it.
This is the solution of The Amazing Race at hackerearth.com


'''



for _ in range(int(input())):
    n=int(input())
    h=[int(h) for h in input().split()]
    back=[0]*n
    sb=[0]
    front=[0]*n
    fb=[n-1]
    for i in range(1,n):
        while len(sb) >0 and h[i]>h[sb[-1]]:
            sb.pop()
        if len(sb)> 0:
            back[i]=i-sb[-1]
        else:
            back[i]=i
        sb.append(i)
    for i in range(n-2,-1,-1):
        while len(fb) > 0 and h[i]>h[fb[-1]]:
            fb.pop()
        if len(fb)>0:
            front[i] =fb[-1] - i  
        else:
            front[i]=n-i-1
        fb.append(i)
    smax=-1
    winner=-1
    for i in range(0,n):
        s=(((back[i]+front[i])%1000000007)*(i+1))%1000000007
        if s>smax:
            smax=s
            winner=i+1
    
    print(winner)
        
        
        
        