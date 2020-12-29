package DataStructures.AssociativeArrays;

import java.util.Arrays;

/*
 * | Maximum Heap (Abstract Data Type) |
 * 
 * - Running Times -
 * 
 * Find maximum/minimum: O(1)
 * Remove maximum/minimum: O(logN)
 * Insert: O(logN)
 * 
 * - Memory Complexity -
 * 		   O(N)
 * 
 *  Rule for parent-child relationship
 *            parent index: 
 *    			   i
 *	 			/     \
 *	 L child index:   R child index:
 *	 	2i + 1			  2i + 2
 */

public class Heap {
	
	private int capacity;
	private int[] heap;
	private int heapSize;
	
	// Non-Default constructor
	public Heap(int capacity) {
		this.heap = new int[capacity];
		this.capacity = capacity;
		this.heapSize = 0;
	}
	
	// Public Methods
	public void insert(int n) {
		// Insert item at counter (heapSize) and increment counter
		if (this.heapSize != this.capacity) {
			this.heap[this.heapSize] = n;
			this.heapSize++;
			// Now check for violations
			this.fixUp(this.heapSize - 1);
		}
	}
	
	public int poll() {
		int max = this.getMax();
		// Swap max with last item of heap
		this.swap(0, this.heapSize - 1);
		// We are no longer able to access max item 
		// because we have decremented the counter.
		// "Soft Delete"
		this.heapSize--;
		this.fixDown(0);
		return max;
	}
	
	public int getMax() {
		return this.heap[0];
	}
    
    // Returns a new array with all elements sorted ascending
	public int[] heapSort() {
        int count = this.heapSize;
        int[] sortedArray = new int[count];
		for (int i = 0; i < count; i++) {
			sortedArray[i] = this.poll();
		}
		return sortedArray;
	}
	
	// Private Methods
	private void fixUp(int index) {
		int parentIndex = Math.floorDiv(index - 1, 2);
		// If the parent is smaller than the child, 
		// swap them and continue up the tree
		if (index > 0 && this.heap[index] > this.heap[parentIndex]) {
			this.swap(index, parentIndex);
			this.fixUp(parentIndex);
		}
	}
	
	private void fixDown(int index) {
		int leftChildIndex = 2 * index + 1;
		int rightChildIndex = 2 * index + 2;
        int largestIndex = index;
        // Find out if one of the children is larger, then swap them
		if (leftChildIndex < this.heapSize && this.heap[leftChildIndex] > this.heap[largestIndex]) {
			largestIndex = leftChildIndex;
		}
		if (rightChildIndex < this.heapSize && this.heap[rightChildIndex] > this.heap[largestIndex]) {
			largestIndex = rightChildIndex;
		}
		if (largestIndex != index) {
			this.swap(largestIndex, index);
			this.fixDown(largestIndex);
		}
	}
	
	private void swap(int i, int j) {
		int temp = this.heap[i];
		this.heap[i] = this.heap[j];
		this.heap[j] = temp;
	}
	
	// Test Client
	public static void main(String[] args) {
		Heap heap = new Heap(10);
		heap.insert(10);
		heap.insert(2);
		heap.insert(100);
		heap.insert(55);
		heap.insert(200);
		heap.insert(5);
		heap.insert(6);
		heap.insert(99);
		heap.insert(500);
		System.out.println(heap.getMax());
        int[] sortedArray = heap.heapSort();
        System.out.println(Arrays.toString(sortedArray));
	}
}
