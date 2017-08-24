def mergerSort(array,start,end):
	if start<end:
		mid = (start+end)//2
		mergerSort(array,start,mid)
		mergerSort(array,mid+1,end)
		merge(array,start,mid,end)

def merge(array,start,mid,end):
	nL=mid-start+1
	nR=end-mid
	leftArray=[]
	rightArray=[]
	for i in range(nL):
		leftArray.append(array[start+i])
	for j in range(nR):
		rightArray.append(array[mid+j+1])
	i,j,k=0,0,start
	while i<nL and j<nR:
		if leftArray[i]<=rightArray[j]:
			array[k]=leftArray[i]
			test.append(i+1)
			i+=1
		else:
			array[k]=rightArray[j]
			j+=1
			test.append(nL+j+1)
		k+=1
	while i<nL:
		array[k]=leftArray[i]
		test.append(i+1)
		i+=1
		k+=1
	while j<nR:
		array[k]=rightArray[j]
		test.append(nL+j+1)
		j+=1
		k+=1


cost=[]
test=[]
for _ in range(int(input())):
	t,s=[int(x) for x in input().split()]
	rate = s/t
	cost.append(rate)

mergerSort(cost,0,len(cost)-1)
print(test)

