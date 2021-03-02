package DataStructures.LinkedLists.LinkedList;

import java.util.NoSuchElementException;

public class LinkedList {

    Node head = null;
    int size = 0;

    private class Node {
        
        Object data;
        Node next;
        
        public Node(Object data) {
            this.data = data;
            this.next = null;
        }
    }

    public int getSize() {
        return size;
    }

    public void insertFront(Object data) {
        size++;
        if (this.head == null) this.head = new Node(data);
        else {
            Node newNode = new Node(data);
            newNode.next = head;
            head = newNode;
        }
    }

    public Object removeFront() {
        if (head == null) throw new NoSuchElementException("List is empty.");
        size--;
        Object data = head.data;
        head = head.next;
        return data;
    }

    public void insertEnd(Object data) {
        size++;
        if (head == null) head = new Node(data);
        else {
            Node n = head;
            while (n.next != null) n = n.next;
            n.next = new Node(data);
        }
    }

    public Object removeEnd() {
        if (head == null) throw new NoSuchElementException("List is empty");
        size--;
        Node n = head;
        Node prev = null;
        while (n.next != null) { // iterate to end of list
            prev = n;
            n = n.next; 
        }
        Object data = n.data;
        if (prev == null) head = null;  // head is node to remove
        else prev.next = null;          // set last node to null
        return data;
    }

    public void traverse() {
        Node n = head;
        while (n != null) {
            System.out.println(n.data);
            n = n.next;
        }
    }

    // Test Client
    public static void main(String[] args) {
        LinkedList ll = new LinkedList();
        ll.insertFront(300);
        ll.insertFront(200);
        ll.insertFront(100);
        ll.insertEnd(400);
        ll.insertEnd(500);
        ll.insertEnd(600);
        ll.traverse();
        System.out.println("Size: " + String.valueOf(ll.getSize()));
        System.out.println("-------");
        ll.removeEnd();
        ll.removeFront();
        ll.traverse();
        System.out.println("Size: " + String.valueOf(ll.getSize()));
    }
}