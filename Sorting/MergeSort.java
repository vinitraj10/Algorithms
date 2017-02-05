import java.util.*;
public class MergeSort{
	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);
		System.out.println("Enter the Size of the List");
		int n=input.nextInt();
		int a[] = new int [n];
		for(int i=0;i<n;i++)
			a[i]=input.nextInt();
		mergesort(a,0,n-1);
		System.out.println("Here is the Sorted list using Mergesort");
		for(int i =0;i<n;i++)
			System.out.print(a[i]+ " ");
	}
	public static void mergesort(int a[],int p,int r){
		if(p<r){
			int q = (int)((p+r)/2);
			mergesort(a,0,q);
			mergesort(a,q+1,r);
			merge(a,p,q,r);
		}
	}
	public static void merge(int a[],int p,int q,int r){
		int n1,n2;
		n1=q-p+1;
		n2=r-q;
		int l[] = new int [n1];
		int d[] = new int [n2];
		for(int i=0;i<n1;i++)
			l[i]=a[p+i];
		for(int j=0;j<n2;j++)
			d[j]=a[q+j+1];
		int i=0;
		int j=0;
		int k = p;
		while(i<n1 && j<n2){
			if(l[i]<=d[j]){
				a[k]=l[i];
				i++;
			}
			else{
				a[k]=d[j];
				j++;
			}
			k++;
		}
		while(i<n1){
			a[k]=l[i];
			i++;
			k++;
		}
		while(j<n2){
			a[k]=d[j];
			j++;
			k++;
		}
	}
}