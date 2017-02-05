public class List{
	static class ListNode{
		int data;
		ListNode next;
	}
	public static void main(String[] args) {
		ListNode l1 = new ListNode();
		ListNode l2 = new ListNode();
		ListNode l3 = new ListNode();
		l1.data=7;
		l2.data=6;
		l3.data=5;
		l1.next=l2;
		l2.next=l3;
		l3.next=null;
		while(l1!=null){
			System.out.println(l1.data);
			l1=l1.next;
		}
	}
}