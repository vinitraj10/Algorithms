#include <stdio.h>

int binarySearch(int a[],int low,int high,int num){
	int mid = (low+high)/2;
	if(low<high){
		if (a[mid] == num){
			return 1;
		}
		else if(num>a[mid])
			return binarySearch(a,mid+1,high,num);
		
		else{
			//printf("THIS REC CALLED");
			return binarySearch(a,low,mid-1,num);
		}
	}
	else if (low==high){
		if (a[low]==num)
			return 1;
		else
			return 0;
	}
	return 0;

}

int main(){
	int n,i,result,num;
	printf("Enter the size of the array :-\n");
	scanf("%d",&n);
	int a[n];
	for(i=0;i<n;i++)
		scanf("%d",&a[i]);
	printf("Enter the number to be Searched :-\n");
	scanf("%d",&num);
	result = binarySearch(a,0,n-1,num);
	if(result ==1)
		printf("Found \n");
	else
		printf("Not Found \n");
}