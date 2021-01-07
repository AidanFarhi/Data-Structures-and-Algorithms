package DataStructures.AssociativeArrays;

import java.util.NoSuchElementException;

/**
 * Whe creating an array, Specify type of array using <> notation.
 * Ex) 
 * DynamicArray<String> = new DynamicArray<>(); for a String array.
 * DynamicArray<Integer> = new DynamicArray<>(); for an Integer array.
 */
public class DynamicArray<Item> {

    private int INITIAL_SIZE = 8;
    private Item[] arr;
    private int size;

    /**
     * Creates an empty array with size 8.
     */
    public DynamicArray() {
        arr = (Item[]) new Object[INITIAL_SIZE];
        size = 0;
    }

    /**
     * Checks if array is empty.
     */
    public boolean isEmpty() {
        return size == 0;
    }

    /**
     * Gets item at specified index.
     */
    public Item itemAt(int index) {
        if (index < 0 || isEmpty() || index > size - 1) throw new IndexOutOfBoundsException();
        return arr[index];
    }

    /**
     * Adds an item to the array.
     */
    public void push(Item item) {
        if (size == arr.length) resize(arr.length * 2);
        arr[size++] = item;
    }

    /**
     * Removes item from end of array.
     */
    public Item pop() {
        if (isEmpty()) throw new NoSuchElementException("Array is empty.");
        Item item = arr[size - 1];
        arr[--size] = null; // Avoid loitering
        if (size > 0 && size == arr.length / 4) resize(arr.length / 2);
        return item;
    }

    /**
     * Resizes array. Copies all items from old array to new one.
     */
    private void resize(int newSize) {
        Item[] newArray = (Item[]) new Object[newSize];
        for (int i = 0; i < size; i++) {
            newArray[i] = arr[i];
        }
        arr = newArray;
    }

    /* Test Client */
    public static void main(String[] args) {
        
    }
}
