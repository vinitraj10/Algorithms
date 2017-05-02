import java.io.*;
import java.util.*;
public class Stacks{
	public static void main(String[] args) {
		Stack<Integer> = new Stack<Integer> ();
		stack_push(stack);
		stack_pop(stack);
		stack_push(stack);
		stack_peek(stack);
		stack_search(stack,2);
		stack_search(stack,3);
	}
	static void stack_push(Stack<Integer> stack){
		for(int i = 1;i<5;i++)
			stack.push(i);
	}
	static void stack_pop(Stack<Integer> stack){
		System.out.println("Pop:");
		for(int i=1;i<=5;i++){
			Integer y = (Integer)stack.pop;
			System.out.println(y);
		}	
	}
	static void stack_peek(Stack<Integer> stack){
		Integer element = (Integer)stack.peek;
		System.out.println("The Top Of The stack is " + element);
	}
	static void stack_search(Stack<Integer> stack, int element)
    {
        Integer pos = (Integer) stack.search(element);
 
        if(pos == -1)
            System.out.println("Element not found");
        else
            System.out.println("Element is found at position " + pos);
    }
}