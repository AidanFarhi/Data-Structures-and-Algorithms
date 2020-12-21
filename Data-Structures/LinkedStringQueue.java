/*
 * Queue
 * 
 * FIFO principle (First In First Out)
 * 
 * This implementation uses a Linked List as an underlying 
 * data structure.
 * 
 */

public class LinkedStringQueue {
	
	private Node head, tail;
	
	private class Node {
		String value;
		Node next;
	}
	
	public boolean isEmpty() {
		return head == null;
	}
	
	// Add new items to end
	public void enqueue(String data) {
		Node oldTail = tail;
		tail = new Node();
		tail.value = data;
		tail.next = null;
		if (isEmpty()) {
			head = tail;
		} else {
			oldTail.next = tail;
		}
	}
	
	// Remove items from the front
	public String dequeue() {
		String item = head.value;
		head = head.next;
		if (isEmpty()) {
			tail = null;
		}
		return item;
	}
}