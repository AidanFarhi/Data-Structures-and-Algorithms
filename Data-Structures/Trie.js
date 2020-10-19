/*
- Trie -

A tree with as many pointers from every node as the number of
characters in the alphabet.

Applications:
- Auto complete
*/

class Node {
    constructor(char) {
        this.char = char
        this.children = {}
        this.endOfWord = false
    }
}

class Trie {
    constructor() {
        this.root = new Node('*')
    }

    insert(word) {
        let current = this.root
        for (let char of word) {
            if (current.children.hasOwnProperty(char)) {
                current = current.children[char]
            } else {
                let newNode = new Node(char)
                current.children[char] = newNode
                current = newNode
            }
        }
        current.endOfWord = true
    }

    search(word) {
        if (this.root.children === null) {
            return false
        }
        let current = this.root
        for (let char of word) {
            if (current.children.hasOwnProperty(char)) {
                current = current.children[char]
            } else {
                return false
            }
        }
        if (current.endOfWord) {
            return true
        } else {
            return false
        }
    }
}

const trie = new Trie()
trie.insert('hello')
trie.insert('goodbye')
console.log(trie.search('hello'))
console.log(trie.search('hell'))
console.log(trie.search('goodbye'))
console.log(trie.search('good'))
