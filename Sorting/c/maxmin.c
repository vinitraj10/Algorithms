#include <stdio.h>
typedef struct{
	int min;
	int max;
}tuple;

tuple maxmin(int a[],int left,int right){
	tuple min_max,min_max_left,min_max_right;
	int mid;
	if(left==right){
		min_max.min=a[left];
		min_max.max=a[right];
		return min_max;
	}
	else if(right==left+1){
		if(a[left]>a[right]){
			min_max.min=a[right];
			min_max.max=a[left];
			return min_max;
		}
		else{
			min_max.min=a[left];
			min_max.max=a[right];
			return min_max;
		}
	}
	mid=(left+right)/2;
	min_max_left=maxmin(a,left,mid);
	min_max_right=maxmin(a,mid+1,right);
	if(min_max_left.min<min_max_right.min){
		min_max.min=min_max_left.min;
	}
	else{
		min_max.min=min_max_right.min;
	}

	if(min_max_left.max<min_max_right.max){
		min_max.max=min_max_left.max;
	}
	else{
		min_max.max=min_max_right.max;
	}
	return min_max;
}

int main(){
	int n,i;
	tuple min_max;
	printf("Enter the size of the list \n");
	scanf("%d",&n);
	int a[n];
	printf("Enter the elements\n");
	for(i=0;i<n;i++)
		scanf("%d",&a[i]);
	min_max= maxmin(a,0,n-1);
	printf("minimum is %d ",min_max.min);
	printf("maximum is %d ",min_max.max);
}