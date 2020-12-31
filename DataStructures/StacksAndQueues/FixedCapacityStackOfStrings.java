package DataStructures.StacksAndQueues;

public class FixedCapacityStackOfStrings {

    private String[] stack;
    private int N = 0;

    public FixedCapacityStackOfStrings(int capacity) {
        stack = new String[capacity];
    }

    public boolean isEmpty() {
        return N == 0;
    }

    public void push(String item) {
        stack[N++] = item; // first uses N as index, then increments N
    }

    public String pop() {
        String item = stack[--N]; // first decrements N, then uses N as an index
        stack[N] = null; // avoids loitering
        return item;
    }
}
