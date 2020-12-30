package DataStructures.UnionFind;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.IOException;
import java.util.Arrays;

public class QuickUnion {
    /*
    * Maintain an array of roots. Entry == root | Index == object id
    */
    private int[] roots;
    /*
    * Constructor | O(N)
    */
    public QuickUnion(int size) {
        roots = new int[size];
        for (int i = 0; i < size; i++) { // Initialize every object to be it's own root
            roots[i] = i;
        }
    }
    /*
    * If roots are equal, objects are connected | O(N)
    */
    public boolean connected(int p, int q) {
        return root(p) == root(q);    
    }
    /*
    * Set qRoot == pRoot | O(N) worst case
    */
    public void union(int p , int q) {
        int pRoot = root(p);
        int qRoot = root(q);
        roots[qRoot] = pRoot;
    }
    public void showRoots() {
        System.out.println(Arrays.toString(roots));
    }

    /*
    * Keep iterating until index == entry, because every object is it's own root
    */
    private int root(int n) {
        while (n != roots[n]) {
            n = roots[n];
        }
        return n;
    }
    /*
    * Test Client
    */
    public static void main(String args[]) throws IOException {
        File testFile = new File(System.getProperty("user.dir") + "/Tests/UF10.txt");
        BufferedReader br = new BufferedReader(new FileReader(testFile));
        int size = Integer.parseInt(br.readLine());
        QuickUnion qu = new QuickUnion(size);
        String pair = br.readLine();
        while (pair != null) {
            int p = Integer.parseInt(pair.substring(0, 1));
            int q = Integer.parseInt(pair.substring(2));
            if (qu.connected(p, q)) {
                System.out.println("[" + p + ", " + q + "] " + "are already connected.");
            } else {
                qu.union(p, q);
                System.out.println("[" + p + ", " + q + "] " + "are now connected.");
            }
            pair = br.readLine();
        }
        br.close();
    }
}