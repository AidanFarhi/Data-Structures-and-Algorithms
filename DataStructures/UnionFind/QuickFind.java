package DataStructures.UnionFind;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.IOException;

public class QuickFind {
    /*
    * Maintain an integer array of size N where N == number of objects.
    * Index == Object id
    * Array entry == Root
    * If two objects have the same root, they are connected.
    */
    private int[] root;

    /*
    * Constructor
    * O(N)
    */
    public QuickFind(int size) {
        root = new int[size];
        for (int i = 0; i < size; i++) { // Set each object's root to itself
            root[i] = i;
        }
    }

    /*
    * Check if objects are connected
    * O(1)
    */
    public boolean connected(int p, int q) {
        return root[p] == root[q];
    }

    /*
    * To connect two objects, we change all entries of root[q] to equal root[p]
    * O(N)
    */
    public void union(int p, int q) {
        if (!connected(p, q)) {
            int pRoot = root[p];
            int qRoot = root[q];
            for (int i = 0; i < root.length; i++) {
                if (root[i] == qRoot) {
                    root[i] = pRoot;
                }
            }
        }
    }

    /*
     * Test Client: 
     * - Read in pairs of integers from standard input. 
     * - If they are not yet connected, connect them and print out pair
     */
    public static void main(String args[]) throws IOException {
        File testFile = new File(System.getProperty("user.dir") + "/Tests/UF10.txt");
        BufferedReader br = new BufferedReader(new FileReader(testFile));
        int size = Integer.parseInt(br.readLine());
        QuickFind qf = new QuickFind(size);
        String pair = br.readLine();
        while (pair != null) {
            int p = Integer.parseInt(pair.substring(0, 1));
            int q = Integer.parseInt(pair.substring(2));
            if (qf.connected(p, q)) {
                System.out.println("[" + p + ", " + q + "] " + "are already connected.");
            } else {
                qf.union(p, q);
                System.out.println("[" + p + ", " + q + "] " + "are now connected.");
            }
            pair = br.readLine();
        }
        br.close();
    }
}
