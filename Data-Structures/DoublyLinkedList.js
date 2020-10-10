class Node {
    constructor(data) {
        this.data = data
        this.next = null
        this.prev = null
    }
}
class DLL {
    constructor() {
        this.head = null
        this.size = 0
    }
    insertStart(data) {
        this.size++
        if (this.head === null) {
            this.head = new Node(data)
        } else {
            const newNode = new Node(data)
            newNode.next = this.head
            this.head.prev = newNode
            this.head = newNode
        }
    }
    removeStart() {
        if (this.head === null) return null
        if (this.head.next === null) {
            const data = this.head.data
            this.head = null
            return data
        } else {
            const data = this.head.data
            this.head.next.prev = null
            this.head = this.head.next
            return data
        }
    }
    traverse() {
        if (this.head === null) return
        let access = this.head
        while (access.next !== null) {
            console.log(access.data)
            access = access.next
        }
        console.log(access.data)
    }
}

const dll = new DLL()

dll.insertStart(1)
dll.insertStart(2)
dll.insertStart(3)
dll.insertStart(4)
dll.insertStart(5)
dll.insertStart(6)
dll.insertStart(7)

dll.traverse()
console.log('------- After Removal -------')

dll.removeStart()
dll.removeStart()
dll.removeStart()

dll.traverse()
