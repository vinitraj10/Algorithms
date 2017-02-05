import java.util.*;

public class SelectionSort{
	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);
		System.out.println("Enter the Size of the List");
		int n=input.nextInt();
		int a[] = new int [n];
		for(int i = 0;i<n;i++)
			a[i]=input.nextInt();
		SelectionSort ob = new SelectionSort();
		ob.sort(a,n);
		System.out.println("Sorted Array Using Bubble sort");
		for(int i =0;i<n;i++){
			System.out.println(a[i]+" ");
		}
	}
	void sort(int a[],int n){
		for(int i =0;i<n-1;i++){
			int min_idx=i;
			for(int j=i+1;j<n;j++){
				if(a[j]<a[min_idx]){
					min_idx=j;
				}
			}
			int temp =a[i];
				a[i]=a[min_idx];
				a[min_idx]=temp;	
		}
			
		}
}