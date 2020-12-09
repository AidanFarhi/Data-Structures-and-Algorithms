/*
- LRU Cache -

A cache is a hardware or software component that stores data so that future requests for that data can be served faster; 
the data stored in a cache might be the result of an earlier computation or a copy of data stored elsewhere.

What Is An LRU Cache?

So a LRU Cache is a storage of items so that future access to those items can be serviced quickly 
and an LRU policy is used for cache eviction.

The Constraints/Operations

Lookup of cache items must be O(1)
Addition to the cache must be O(1)
The cache should evict items using the LRU policy

The Approach

There are many ways to do this but the most common approach is to use 2 critical structures: 
a doubly linked list and a hashtable.

Our Structures
Doubly Linked List: This will hold the items that our cache has. We will have n items in the cache.
This structure satisfies the constraint for fast addition since any doubly linked list item can be added or removed in 
O(1) time with proper references.

Hashtable: 
The hashtable will give us fast access to any item in the doubly linked list items to avoid O(n) search for items and 
the LRU entry (which will always be at the tail of the doubly linked list).
This is a very common pattern, we use a structure to satisfy special insertion or 
remove properties (use a BST, linked list, etc.) and back it up with with a 
hashtable so we do not re-traverse the structures every time to find elements.


Complexities
Time
Both get and put methods are O( 1 ) in time complexity.
Space
We use O( n ) space since we will store n items where n ist the capacity of the cache.

*/

import java.util.HashMap;

public class LRUCache {
	
	// Essentially a DLL Node
	public class LRUNode {
		
		// Initial values
		private int key = 0;
		private int value = 0;
		private LRUNode next = null;
		private LRUNode prev = null;
		
		// Default Constructor
		public LRUNode() {
			
		}
		
		// Constructor when user wants to set keys and values
		public LRUNode(int key, int value) {
			this.key = key;
			this.value = value;
		}
		
		// Getters and Setters
		public int getKey() { return key; }
		public void setKey(int key) { this.key = key; }
		public int getValue() { return value; }
		public void setValue(int value) { this.value = value; }
		public LRUNode getNext() { return next; }
		public void setNext(LRUNode next) { this.next = next; }
		public LRUNode getPrev() { return prev; }
		public void setPrev(LRUNode prev) { this.prev = prev; }
	}
	
	// This is the cache that stores the keys and nodes
	HashMap<Integer, LRUNode> cache = new HashMap<Integer, LRUNode>();
	// Capacity will be initialized when LRU instance is created
	int capacity;
	int size = 0;
	// Dummy Head and Tail nodes
	LRUNode head = new LRUNode();
	LRUNode tail = new LRUNode();
	
	// Constructor
	public LRUCache(int capacity) {
		this.capacity = capacity;
		this.head.setNext(this.tail);
		this.tail.setPrev(this.head);
	}
	
	// The 3 public methods will be put(), get(), and showCache()
	public void put(int key, int value) {
		LRUNode node = this.cache.get(key);
		if (node != null) {
			node.setValue(value);
			this.moveToHead(node);
		} else {
			LRUNode newNode = new LRUNode(key, value);
			this.addNode(newNode);
			this.cache.put(key, newNode);
			this.size++;
			if (this.size > this.capacity) {
				LRUNode tail = this.popTail();
				this.cache.remove(tail.getKey());
				this.size--;
			}
		}
	}
	
	public int get(int key) {
		LRUNode node = this.cache.get(key);
		if (node != null) {
			this.moveToHead(node);
			return node.getValue();
		}
		return -1;
	}
    
    // Returns an array representation of cached values and their respective positions
	public int[] showCache() {
		int[] cacheValues = new int[this.capacity];
		LRUNode current = this.head.getNext();
		int i = 0;
		while (current != this.tail) {
			cacheValues[i] = current.getValue();
			current = current.getNext();
			i++;
		}
		return cacheValues;
	}
	
	// Private methods
	private LRUNode popTail() {
		LRUNode tail = this.tail.getPrev();
		this.removeNode(tail);
		return tail;
	}

	private void removeNode(LRUNode node) {
		LRUNode prev = node.getPrev();
		LRUNode next = node.getNext();
		prev.setNext(next);
		next.setPrev(prev);
	}

	private void addNode(LRUNode newNode) {
		// Always add right after head
		newNode.setPrev(this.head);
		LRUNode next = this.head.getNext();
		this.head.setNext(newNode);
		newNode.setNext(next);
		next.setPrev(newNode);
	}

	private void moveToHead(LRUNode node) {
		this.removeNode(node);
		this.addNode(node);
	}
}
