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
        let accessNode = this.head

        while (accessNode.nextNode !== null) {
            accessNode = accessNode.nextNode
        }
        accessNode.nextNode = newNode
    }
    remove(data) {
        if (this.head === null) return

        let accessNode = this.head
        let previousNode = null

        while (accessNode !== null && accessNode.data !== data) {
            previousNode = accessNode
            accessNode = previousNode.nextNode
        }

        if (accessNode === null) {
            return
        } else {
            this.size++
            if (previousNode === null) {
                this.head = accessNode.nextNode
            } else {
                previousNode.nextNode = accessNode.nextNode
            }
        }
    }
    getSize() {
        return this.size
    }
    printNodes() {
        let accessNode = this.head

        while (accessNode !== null) {
            console.log(accessNode.data)
            accessNode = accessNode.nextNode
        }
    }
}
