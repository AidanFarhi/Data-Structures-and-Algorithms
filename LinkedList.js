class Node {
    constructor(data) {
        this.data = data
        this.nextNode = null
    }
}
class LinkedList {
    constructor() {
        this.head = null
        this.size = 0
    }
    // Methods
    insertStart(data) {
        this.size++
        let newNode = new Node(data)
        if (this.head === null) {
            this.head = newNode
        } else {
            newNode.nextNode = this.head
            this.head = newNode
        }
    }
    insertEnd(data) {
        this.size++
        let newNode = new Node(data)
        let searchNode = this.head
        while (searchNode.nextNode !== null) {
            searchNode = searchNode.nextNode
        }
        searchNode.nextNode = newNode
    }
    getSize() {
        return this.size
    }
    printNodes() {
        let searchNode = this.head
        while (searchNode !== null) {
            console.log(searchNode.data)
            searchNode = searchNode.nextNode
        }
    }
}
