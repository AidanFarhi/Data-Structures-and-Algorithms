package DataStructures.Trees.BinarySearchTree;
/*
- Binary Search Tree -
- Keeps the keys in sorted order so that look up and other operations can use
  binary search
- Each comparison allow the operations to skip over half of the tree, so
  that each lookup/insertion/deletion takes time proportional to the logarithm
  of the number of items stored in the tree O(log N)
- This is much better than the linear time O(N) required to find items by key
  in an unsorted array, but slower than the operations in hash tables
- Every node can have at most two children. Left and Right.
  Left child < Parent
  Right child > Parent
*/
import java.util.ArrayList;

public class BST<Key extends Comparable<Key>, Value> {

    private Node root;

    private class Node {
        private Key key;
        private Value val;
        private Node left, right;
        private int count;
        public Node(Key key, Value val) {
            this.key = key;
            this.val = val;
        }
    }

    public void put(Key key, Value val) {
        root = putHelper(root, key, val);
    }

    private Node putHelper(Node x, Key key, Value val) {
        if (x == null) return new Node(key, val);
        int cmp = key.compareTo(x.key);
        if (cmp < 0) {
            x.left = putHelper(x.left, key, val);
        } else if (cmp > 0) {
            x.right = putHelper(x.right, key, val);
        } else {
            x.val = val;
        }
        x.count = 1 + getSize(x.left) + getSize(x.right);
        return x;
    }

    public Value get(Key key) {
        Node x = root;
        while (x != null) {
            int cmp = key.compareTo(x.key);
            if (cmp < 0) x = x.left;
            else if (cmp > 0) x = x.right;
            else return x.val;
        }
        return null;
    }

    public Node getMin() {
        return getMinHelper(root);
    }

    private Node getMinHelper(Node x) {
        if (x.left == null) return x;
        return getMinHelper(x.left);
    }

    public void delete(Key key) {
        root = deleteHelper(root, key);
    }

    private Node deleteHelper(Node x, Key key) {
        if (x == null) return null;
        int cmp = key.compareTo(x.key);
        if (cmp < 0) x.left = deleteHelper(x.left, key);
        else if (cmp > 0) x.right = deleteHelper(x.right, key);
        else {
            if (x.right == null) return x.left; // no right child
            if (x.left == null) return x.right; // no left child
            Node t = x;
            x = getMinHelper(t.right);
            x.right = deleteMinHelper(x.right);
            x.left = t.left;
        }
        x.count = getSize(x.left) + getSize(x.right) + 1;
        return x;
    }

    public void deleteMin() {
        root = deleteMinHelper(root);
    }

    private Node deleteMinHelper(Node x) {
        if (x.left == null) return x.right;
        x.left = deleteMinHelper(x.left);
        x.count = 1 + getSize(x.left) + getSize(x.right);
        return x;
    }

    // Implement size method here
    public int size() {
        return getSize(root);
    }

    private int getSize(Node x) {
        if (x == null) return 0;
        return x.count;
    }

    public Iterable<Key> keys() {
        ArrayList<Key> l = new ArrayList<>();
        inorderKey(root, l);
        return l;
    }

    private void inorderKey(Node x, ArrayList<Key> l) {
        if (x == null) return;
        inorderKey(x.left, l);
        l.add(x.key);
        inorderKey(x.right, l);
    }

    public Iterable<Value> values() {
        ArrayList<Value> l = new ArrayList<>();
        inorderValue(root, l);
        return l;
    }

    private void inorderValue(Node x, ArrayList<Value> l) {
        if (x == null) return;
        inorderValue(x.left, l);
        l.add(x.val);
        inorderValue(x.right, l);
    }

    public static void main(String[] args) {
        BST<Integer, String> bst = new BST<>();
        bst.put(50, "Alan");
        bst.put(10, "Bob");
        bst.put(78, "Jimmy");
        bst.put(34, "Lue");
        bst.put(89, "Fred");
        bst.put(13, "Ted");
        bst.put(11, "Billy");
        bst.put(57, "Yori");
        bst.put(98, "Nola");
        bst.put(24, "Dia");
        Iterable keys = bst.keys();
        Iterable vals = bst.values();
        System.out.println("Inorder keys and values:");
        for (Object key: keys) {
            System.out.println(bst.get((Integer)key));
            System.out.println(key.toString());
        }
        System.out.println("Inorder values:");
        for (Object val: vals) {
            System.out.println(val.toString());
        }
        System.out.println("Tree Size: " + String.valueOf(bst.size()));
    }
}