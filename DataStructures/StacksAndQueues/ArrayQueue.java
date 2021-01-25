package DataStructures.StacksAndQueues;
import java.util.Arrays;

/**
 * A Dynamically resizing Queue
 */
class ArrayQueue<Item> {

    // Initialize a Queue of size 2, and a pointer to head, tail, and a record of size and capacity
    private Item[] queue = (Item[]) new Object[2];
    private int head, tail, size = 0;
    private int capacity = 2;

    /**
     * Add an item to the Queue
     * @param item
     */
    public void enqueue(Item item) {
        if (size == capacity) { resize(capacity * 2); }
        size++;
        queue[tail++] = item;
        if (tail == capacity) { tail = 0; } // Wrap around once tail reaches end of array
    }

    /**
     * Remove the next Item from the Queue
     * @return Item
     */
    public Item dequeue() {
        if (size == 0) { return null; }
        Item item = queue[head++];
        queue[head - 1] = null; // Avoid loitering
        size--;
        if (size > 0 && size == capacity / 4) { resize(capacity / 2); }
        if (head == capacity) { head = 0; } // Wrap around once head reaches end of array
        return item;
    }

    /**
     * Resizes underlying array to given newSize
     * @param newSize
     */
    private void resize(int newSize) {
        // Copy items from old array to new array
        Item[] copy = (Item[]) new Object[newSize];
        int count = 0;
        while (count < size) {
            copy[count] = queue[head];
            if (head == capacity - 1) { 
                head = 0; 
            } else {
                head++;
            }
            count++;
        }
        // Reset pointers and capacity
        capacity = newSize;
        head = 0;
        tail = size;
        queue = copy;
    }

    /**
     * Prints the underlying array to console
     */
    public void showQueue() {
        System.out.println(Arrays.toString(queue));
    }

    /* Test client */
    public static void main(String[] args) {
        ArrayQueue<String> q = new ArrayQueue<>();
        System.out.println("-- Queue with nothing in it --");
        q.showQueue();
        q.enqueue("1");
        q.enqueue("2");
        q.enqueue("3");
        q.enqueue("4");
        q.enqueue("5");
        q.enqueue("6");
        q.enqueue("7");
        q.enqueue("8");
        q.enqueue("9");
        q.enqueue("10");
        q.enqueue("11");
        q.enqueue("12");
        System.out.println("-- Queue after adding 12 items --");
        q.showQueue();
        for (int i = 0; i < 6; i++) {
            System.out.println(q.dequeue());
        }
        System.out.println("-- Queue after removing 6 items --");
        q.showQueue();
        q.enqueue("13");
        q.enqueue("14");
        q.enqueue("15");
        q.enqueue("16");
        System.out.println("-- Queue after adding 4 more items --");
        q.showQueue();
        for (int i = 0; i < 10; i++) {
            System.out.println(q.dequeue());
        }
        System.out.println("-- Queue after emptying all items --");
        q.showQueue();
    }
}