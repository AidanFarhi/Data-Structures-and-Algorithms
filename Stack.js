class Stack {
    constructor() {
        this.stack = []
    }
    push(data) {
        this.stack.push(data)
    }
    pop() {
        if (this.stack.length === 0) return -1

        const data = this.stack[this.stack.length - 1]
        this.stack.pop()
        return data
    }
    peek() {
        return this.stack[this.stack.length - 1]
    }
    getSize() {
        return this.stack.length
    }
    isEmpty() {
        return this.stack.length === 0
    }
}
