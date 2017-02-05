import java.util.*;

public class BubbleSort{
	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);
		System.out.println("Enter the Size of the List");
		int n=input.nextInt();
		int a[] = new int [n];
		for(int i = 0;i<n;i++)
			a[i]=input.nextInt();
		BubbleSort ob = new BubbleSort();
		ob.sort(a,n);
		System.out.println("Sorted Array Using Bubble sort");
		for(int i =0;i<n;i++){
			System.out.println(a[i]+" ");
		}
	}
	void sort(int a[],int n){
		for(int i =0;i<n-1;i++)
			for(int j=0;j<n-1-i;j++){
				if(a[j]>a[j+1]){
					int temp =a[j+1];
					a[j+1]=a[j];
					a[j]=temp;
				}
			}	
		}
}