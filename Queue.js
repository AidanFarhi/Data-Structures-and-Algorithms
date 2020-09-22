class Queue {
    constructor() {
        this.queue = []
    }
    enqueue(data) {
        this.queue.push(data)
    }
    dequeue() {
        if (this.queue.length === 0) return -1
        const data = this.queue[0]
        this.queue.shift()
        return data
    }
    peek() {
        return this.queue[0]
    }
    queueSize() {
        return this.queue.length
    }
    isEmpty() {
        return this.queue.length === 0
    }
}