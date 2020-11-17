"""
- Hash Table -

A hash table is an associative array that enables a 'key' to be
mapped to an index using a hash function.
Python's built in dictionary {} is an example.

+ Running Times +
        - Average -      - Worst Case -
Space       O(N)             O(N)
Insert      O(1)             O(N)
Delete      O(1)             O(N)
Search      O(1)             O(N)
"""

class HashTable:
    # Default size: 10
    def __init__(self, size=10):
        self.size = size
        self.keys = [None] * size
        self.values = [None] * size

    def put(self, key, value):
        index = self.hash_function(key)
        # If index already exists
        while self.keys[index] is not None:
            # If there is a match, then update value
            if self.keys[index] == key:
                self.values[index] = value
                return
            # If there is an index collision, then do linear probing
            index = (index + 1) % self.size
        # Once we have a valid index, now we set our key, value pair
        self.keys[index] = key
        self.values[index] = value
    
    def get(self, key):
        index = self.hash_function(key)
        # Repeat same process of put() method to find the value
        while self.keys[index] is not None:
            if self.keys[index] == key:
                return self.values[index]
            index = (index + 1) % self.size
        # Return None if there is no match
        return None
    
    # This creates an index based on the sum of all
    # chars of the key's ASCII values
    def hash_function(self, key):
        total = 0
        for ch in key:
            total += ord(ch)
        return total % self.size
