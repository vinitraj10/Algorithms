import java.util.*;
class BinarySearch2{
	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);
		System.out.println("Enter the Size of The List");
		int n = input.nextInt();
		int a[] = new int [n];
		for(int i=0;i<n;i++)
			a[i]=input.nextInt();
		System.out.println("Enter the Value to be Searched");
		int key = input.nextInt();
		int result=search(a,0,n-1,key);
		if(result==-1)
			System.out.println("Not Found In the List");
		else
			System.out.println("Found at index " + result);
	}
	static int search(int a[],int l,int h,int key ){
		while(l<=h){
			int mid = (l+h)/2;
			if(a[mid]==key)
				return mid;
			else if(a[mid]>key)
				h=mid-1;
			else
				l=mid+1;
		}
		return -1;
	}
}