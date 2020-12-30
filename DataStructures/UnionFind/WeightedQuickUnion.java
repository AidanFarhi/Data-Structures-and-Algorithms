package DataStructures.UnionFind;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.IOException;

public class WeightedQuickUnion {
    /* Same as QuickUnion, except here we are maintaining an array of size */
    private int[] roots;
    private int[] sizes;

    /* Constructor */
    public WeightedQuickUnion(int size) {
        roots = new int[size];
        sizes = new int[size];
        for (int i = 0; i < size; i++) {
            roots[i] = i;
            sizes[i] = 1;
        }
    }

    /* O(logN) */
    public boolean connected(int p, int q) {
        return getRoot(p) == getRoot(q);
    }

    /* This now becomes a O(logN) operation instead of O(N) */
    public void union(int p, int q) {
        int pRoot = getRoot(p);
        int qRoot = getRoot(q);
        /* 
        * This is the key difference. We always add the smaller
        * connected component to the larger one. Hence: 'Weighted'.
        */
        if (pRoot != qRoot) {
            if (sizes[pRoot] < sizes[qRoot]) { 
                roots[pRoot] = roots[qRoot];
                sizes[qRoot]++;
            } else {
                roots[qRoot] = roots[pRoot];
                sizes[pRoot]++;
            }
        }
    }

    private int getRoot(int n) {
        while (n != roots[n]) {
            /* 
            * One pass path compression. 
            * Make every other node point to it's grandparent. 
            */
            roots[n] = roots[roots[n]];
            n = roots[n];
        }
        return n;
    }

    /* Test Client */
    public static void main(String args[]) throws IOException {
        File testFile = new File(System.getProperty("user.dir") + "/Tests/UF10.txt");
        BufferedReader br = new BufferedReader(new FileReader(testFile));
        int size = Integer.parseInt(br.readLine());
        WeightedQuickUnion wqu = new WeightedQuickUnion(size);
        String pair = br.readLine();
        while (pair != null) {
            int p = Integer.parseInt(pair.substring(0, 1));
            int q = Integer.parseInt(pair.substring(2));
            if (wqu.connected(p, q)) {
                System.out.println("[" + p + ", " + q + "] " + "are already connected.");
            } else {
                wqu.union(p, q);
                System.out.println("[" + p + ", " + q + "] " + "are now connected.");
            }
            pair = br.readLine();
        }
        br.close();
    }
}