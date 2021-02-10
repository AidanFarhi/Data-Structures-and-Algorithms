package DataStructures.StacksAndQueues.Queues;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.IOException;

/* A Priority Queue using a binary heap */

public class MaxPQ<Key extends Comparable<Key>> {

    private Key[] pq;
    private int N;

    public MaxPQ(int capacity) {
        pq = (Key[]) new Comparable[capacity + 1];
        N = 0;
    }

    public boolean isEmpty() {
        return N == 0;
    }

    public void insert(Key k) {
        pq[++N] = k;
        swim(N);
    }

    public Key getMax() {
        return pq[1];
    }

    /**
     * Returns and removes max from priority queue
     */
    public Key delMax() {
        Key max = getMax();
        swap(1, N--);
        sink(1);
        pq[N + 1] = null; // prevent loitering
        return max;
    }

    /**
     * Go up tree and exchage k with parent if k > parent (k/2).
     */
    private void swim(int k) {
        // while k not at root of heap and k > its parent (k/2)
        while (k > 1 && lessThan(k/2, k)) {
            swap(k, k/2);   // swap parent and child
            k = k/2;        // move up the tree
        }
    }

    /**
     * Go down tree and exchange k with larger child. 
     * Children of k are 2k and 2k + 1.
     */
    private void sink(int k) {
        while (2*k <= N) {
            int j = 2*k;    // left child
            if (j < N && lessThan(j, j + 1)) j++; // case where r child is greater
            if (!lessThan(k, j)) break;  // k is larger than both children
            swap(k, j);  // swap k with largest child
            k = j;  // go down tree
        }
    }

    private boolean lessThan(int i, int j) {
        return pq[i].compareTo(pq[j]) < 0;
    }

    private void swap(int i, int j) {
        Key temp = pq[i];
        pq[i] = pq[j];
        pq[j] = temp;
    }

    /* Test Client */
    public static void main(String[] args) throws IOException {
        String test = args[0];
        File testFile = new File(System.getProperty("user.dir") + "/Tests/" + test);
        BufferedReader br = new BufferedReader(new FileReader(testFile));
        Integer size = Integer.parseInt(br.readLine());
        MaxPQ<Integer> pq = new MaxPQ<>(size);
        String next = br.readLine();
        while (next != null) {
            if (next.equals("pop")) {
                System.out.println("Max Item: " + String.valueOf(pq.delMax()));
            } else {
                pq.insert(Integer.parseInt(next));
            }
            next = br.readLine();
        }
        while (!pq.isEmpty()) {
            System.out.println(pq.delMax());
        }
        br.close();
    }
}