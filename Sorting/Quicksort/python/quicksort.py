#!/usr/bin/python3
def partition(a,left,right):
    pivot = a[right]
    k=-1
    for i in range(len(a)):
        if(a[i]<pivot):
            k+=1
            a[k],a[i]=a[i],a[k]
        else:
            pass
    a[k+1],a[right]=a[right],a[k+1]
    return k


def sort(a,left,right):
    if(left<right):
        pi = partition(a,left,right)
        sort(a,left,pi)
        sort(a,pi+1,right)


print("Enter the elements of array")
a = [int(x) for x in input().split()]
sort(a,0,len(a)-1)
print(a)
