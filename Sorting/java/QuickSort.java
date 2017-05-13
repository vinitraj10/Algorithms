import java.util.*;
public class QuickSort{
	 static int partition(int a[],int p,int r){
		int pivot = a[r];
		int i=p-1;
		for(int j = p;j<=r-1;j++){
			if(a[j]<=pivot){
				i++;
				int temp=a[i];
				a[i]=a[j];
				a[j]=a[i];		
			}
		}
		int temp =a[i+1];
		a[i+1]=a[r];
		a[r]=temp;

		return (i+1);
	}
	static void sort(int a[],int p,int r){
		if(p<r){
			int pi = partition(a,p,r);
			sort(a,p,pi-1);
			sort(a,pi+1,r);
		}
	}
	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);
		System.out.println("Enter the Size of the list");
		int n = input.nextInt();
		int a[] = new int [n];
		for(int i =0;i<n;i++)
			a[i]=input.nextInt();
		sort(a,0,n-1);
		System.out.println("Sorted Using QuickSort Method:-");
		for(int i =0;i<n;i++)
			System.out.println(a[i]+" ");
	}
}