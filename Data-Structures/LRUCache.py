"""
- LRU Cache -

What is a Cache?

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

"""


class DLLNode:
    def __init__(self):
        self.key = 0
        self.value = 0
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity):
        self.cache = {}
        self.size = 0
        self.capacity = capacity
        # The head and tail here are dummies:
        # Meaning, they will always be null.
        # We add/remove new nodes between them.
        self.head = DLLNode()
        self.tail = DLLNode()
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def get(self, key):
        node = self.cache.get(key, None)
        if not Node:
            return -1
        # Move accessed node to head
        self.__move_to_head(node)
        return node.value
    
    def put(self, key, value):
        node = self.cache.get(key, None)
        # If there is no node with that key already
        if node is None:
            new_node = DLLNode()
            new_node.key = key
            new_node.value = value
            self.cach[key] = new_node
            self.__add_node(new_node)
            self.size += 1
            # If we go over capacity, bump least recently used node
            if self.size > self.capacity:
                # Get rid of tail node
                tail = self.__pop_tail()
                del self.cache[tail.key]
                self.size -= 1
        else:
            # Update the value of the node at that key
            node.value = value
            # Move to head because it is the most recently used
            self.__move_to_head(node)
    
    def __add_node(self, node):
        # Always add the new node right after the head
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node
    
    def __remove_node(self, node):
        prev = node.prev
        new = node.next
        prev.next = new
        new.prev = prev
    
    def __move_to_head(self, node):
        self.__remove_node(node)
        self.__add_node(node)

    def __pop_tail(self):
        res = self.tail.prev
        self.__remove_node(res)
        return res
