import java.util.*;
class BinarySearch{
	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);
		System.out.println("Enter The Size of the List");
		int n = input.nextInt();
		int a[] =  new int [n];
		for(int i=0;i<n;i++)
			a[i]=input.nextInt();
		System.out.println("Enter the No Which You want To Search");
		int key= input.nextInt();
		BinarySearch object = new BinarySearch();
		int result=object.search(a,0,n-1,key);
		if(result == -1)
			System.out.printf("Element is not present in array");
		else
			System.out.printf("Element is present at index %d", result);
	}
	int search(int a[],int l,int h,int key){
		 if (h >= l){
      	  int mid = (l +h)/2;
        	if (a[mid] == key)
        		return mid;
	        else if (a[mid] > key) 
	        	return search(a, l, mid-1, key);
 	     	else   
 	     		return search(a, mid+1, h, key);
   }
   return -1;
	}
}