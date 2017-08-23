#include <stdio.h>
void swap(int *a,int*b){
	int temp =*a;
	*a=*b;
	*b=temp;
}

int main(){
	int n,j;
	printf("Enter the sizeof array:-\n");
	scanf("%d",&n);
	int a[n];
	for(j=0;j<n;j++)
		scanf("%d",&a[j]);
	int startpos=0,minpos,i;
	for(startpos=0;startpos<6;startpos++){
		minpos=startpos;
		for(i=minpos+1;i<6;i++){
			if(a[i]<a[minpos]){
				minpos=i;
			}
		}
		swap(&a[startpos],&a[minpos]);
	}
	printf("Sorted array:-\n");
	for(i=0;i<n;i++)
		printf("%d ",a[i]);
	return 0;
} 