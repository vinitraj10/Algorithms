import java.util.*;
class Linear{
	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);
		System.out.println("Enter the Size of The List");
		int n = input.nextInt();
		int a[] = new int [n];
		for(int i =0;i<n;i++)
			a[i]=input.nextInt();
		System.out.println("Enter the Value To Be Searched In the List");
		int key = input.nextInt();
		Linear ob = new Linear();
		ob.search(a,n,key);
	}
	void search(int a[],int n,int key){
		int i=0;
		for(i=0;i<n;i++){
			if(a[i]==key){
				System.out.println(key +" Is Found At Position No. " + (i+1)+" ");
				break;
			}
		}
		if(i==n)
			System.out.println(key + " Not Found In the List ");
	}
}