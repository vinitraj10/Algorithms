import java.util.*;
public class Insort{
	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);
		int n;
		System.out.println("Enter the Size of the List");
		n=input.nextInt();
		int a[] = new int[n];
		for(int i=0;i<n;i++)
			a[i]=input.nextInt();
		sort(a,n);
		System.out.println("Sorted Array Using Insertion Sort:-");
		for(int i = 0;i<n;i++)
			System.out.println(a[i] +" " );
	}
	public static void sort(int a[],int n){
		for(int j=1;j<n;j++){
			int key=a[j];
			int i =j-1;
			while(i>-1 && a[i]>key){
				a[i+1]=a[i];
				i--;
			}
			a[i+1]=key;
		}
	}
}