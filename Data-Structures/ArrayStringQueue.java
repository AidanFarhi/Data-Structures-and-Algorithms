import java.util.Arrays;

public class ArrayStringQueue {
	
	private int head, tail;
	private String[] queue;
	private int size;
	
	// Default Constructor
	public ArrayStringQueue() {
		size = 0;
		head = -1;
		tail = -1;
		queue = new String[2]; // Default size 16
	}
	
	public void enqueue(String data) {
		if (tail < 0) {
			tail++;
			head++;
			queue[tail] = data;
		} else {
			tail++;
			if (tail == queue.length - 1) {
				resize(queue.length * 2);
			}
			queue[tail] = data;
		}
		size++;
	}
	
	public String dequeue() {
		if (head < 0 || size == 0) {
			return "Queue Empty";
		} else {
			String data = queue[head];
			head++;
			size--;
			if (size > 0 && size == queue.length / 4) {
				resize(queue.length / 2);
			}
			if (size == 0) {
				queue[tail] = null;
			}
			return data;
		}
	}
	
	public void showItems() {
		System.out.println(Arrays.toString(queue));
	}
	
	private void resize(int newSize) {
		String[] newArray = new String[newSize];
		int index = 0;
		for (int i = head; i <= tail; i++) {
			newArray[index] = queue[i];
			index++;
		}
		head = 0;
		tail = index - 1;
		queue = newArray;
	}
}