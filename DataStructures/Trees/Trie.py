"""
- Trie -

A tree with as many pointers from every node as the number of
characters in the alphabet.

Applications:
- Auto complete
"""

class Node:
    def __init__(self, char):
        self.char = char
        self.children = {}
        self.end_of_word = False


class Trie:
    def __init__(self):
        self.root = Node('*')
    
    def insert(self, word):
        current = self.root
        for char in word:
            if char in current.children:
                current = current.children[char]
            else:
                new_node = Node(char)
                current.children[char] = new_node
                current = new_node
        current.end_of_word = True
    
    def search(self, word):
        if self.root.children is None:
            return False
        current = self.root
        for char in word:
            if char in current.children:
                current = current.children[char]
            else:
                return False
        if current.end_of_word:
            return True
        return False

trie = Trie()
trie.insert('hello')
trie.insert('goodbye')
print(trie.search('hello'))
print(trie.search('hell'))
print(trie.search('goodbye'))
print(trie.search('good'))
