package DataStructures.StacksAndQueues;
/*
 * - Stack -
 * Last In First Out
 * 
 * Operations:
 * 
 * push()
 * pop()
 * iterate()
 * 
 * This implementation uses a LinkedList as an underlying
 * data structure and accepts Strings as a data type.
 */

public class LinkedStringStack {
	
	private Node head = null;
	private int size;
	
	private class Node {
		
		String value;
		Node next;
		
	}
	
	public void push(String item) {
		if (head == null) {
			head = new Node();
			head.value = item;
			head.next = null;
		} else {
			Node oldHead = head;
			head = new Node();
			head.next = oldHead;
			head.value = item;
		}
		size++;
	}
	
	public String pop() {
		if (head != null) {
			String val = head.value;
			head = head.next;
			size--;
			return val;
		} else {
			return "Empty";
		}
	}
	
	public String[] showItems() {
		if (head != null) {
			String[] items = new String[size];
			Node current = head;
			int index = 0;
			while (current != null) {
				items[index] = current.value;
				current = current.next;
				index++;
			}
			return items;
		} else {
			String[] empty = new String[0];
			return empty;
		}
	}
}
