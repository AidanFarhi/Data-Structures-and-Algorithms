package DataStructures.StacksAndQueues.Stacks;

import java.util.Arrays;

public class ArrayStack<Item> {
    
    // Initialize a stack of any given type, and maintain a record of the size and head
    private Item[] stack = (Item[]) new Object[2];
    private int head = 0;
    private int capacity = 2;

    public void push(Item item) {
        if (head == capacity) { resize(capacity * 2); }
        stack[head++] = item;
    }

    public Item pop() {
        if (head == 0) { return null; }
        Item item = stack[--head];
        if (head > 0 && head == capacity / 4) { resize(capacity / 2); }
        return item;
    }

    private void resize(int newSize) {
        capacity = newSize;
        Item[] copy = (Item[]) new Object[newSize];
        for (int i = 0; i < head; i++) {
            copy[i] = stack[i];
        }
        stack = copy;
    }

    public void showItems() {
        System.out.println(Arrays.toString(stack));
    }

    /* Test Client */
    public static void main(String[] args) {
        ArrayStack<Integer> stack = new ArrayStack<>();
        for (int i = 0; i < 10; i++) {
            stack.push(i);
        }
        stack.showItems();
        for (int j = 0; j < 13; j++) {
            System.out.println(stack.pop());
        }
        stack.showItems();
    }
}
