/*
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
*/

class HashTable {
    constructor(size=10) {
        this.size = size
        this.keys = Array(size).fill(null)
        this.values = Array(size).fill(null)
    }

    put(key, value) {
        let index = this.hashFunction(key)
        // If index is already used, either update
        // the value or linear probe for a new index
        while (this.keys[index]) {
            if (this.keys[index] === key) {
                this.values[index] = value
                return
            }
            index = (index + 1) % this.size
        }
        this.keys[index] = key
        this.values[index] = value
    }

    get(key) {
        let index = this.hashFunction(key)
        // Same process as the put() method
        while (this.keys[index]) {
            if (this.keys[index] === key) {
                return this.values[index]
            }
            index = (index + 1) % this.size
        }
        return null
    }

    hashFunction(key) {
        let total = 0
        for (let ch in key) {
            total += ch.charCodeAt(0)
        }
        return total % this.size
    }
}

const ht = new HashTable()
ht.put('hi', 100)
ht.put('bye', 200)
console.log(ht.get('hi'))
console.log(ht.get('bye'))
