const fs = require('fs')

class DynamicArray {
    /**
     * Creates an empty array of size 8.
     */
    constructor() {
        this.arr = Array(8)
        this.size = 0
    }

    /**
     * Checks if array is empty
     */
    isEmpty() {
        return this.size === 0
    }

    /**
     * Adds item to end of array.
     */
    push(item) {
        if (this.size == this.arr.length) this.resize(this.arr.length * 2)
        this.arr[this.size] = item
        this.size++
    }

    /**
     * Removes item from end of array
     */
    pop() {
        if (this.size === 0) throw new Error("Array is empty.")
        const item = this.arr[this.size - 1]
        this.size--
        this.arr[this.size] = null
        if (this.size > 0 && this.size === this.arr.length / 4) this.resize(this.arr.length / 2)
        return item
    }

    /**
     * Resizes array
     */
    resize(newSize) {
        const newArray = Array(newSize)
        for (let i = 0; i < this.size; i++) {
            newArray[i] = this.arr[i]
        }
        this.arr = newArray
    }

    /**
     * Returns item at given index
     */
    itemAt(index) {
        if (this.isEmpty() || index < 0 || index > this.size - 1) throw new Error("Index out of range")
        return this.arr[index]
    }
}

/* Test Section */
function main() {
    fs.readFile(__dirname + '/Tests/arrayTest.txt', 'utf8',
        function(err, data) {
            if (err) throw err
            const array = new DynamicArray()
            const testData = data.split('\n')
            for (let i = 0; i < testData.length; i++) {
                let item = testData[i]
                if (item === '-') {
                    array.pop()
                } else {
                    array.push(item)
                }
            }
            console.log(`Size of array: ${array.size}`) // should be -> 2
            console.log(`Array length: ${array.arr.length}`) // should be -> 4
        }
    )
}

main()
