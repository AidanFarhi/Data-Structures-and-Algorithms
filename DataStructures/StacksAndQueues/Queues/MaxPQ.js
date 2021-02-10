const fs = require('fs')

class MaxPQ {

    constructor(capacity) {
        this.N = 0
        this.capacity = capacity
        this.pq = new Array(capacity + 1)
    }

    isEmpty() {
        return this.N === 0
    }

    insert(item) {
        if (this.N == this.capacity) {
            console.log("pq at max.")
            return
        }
        this.pq[++this.N] = item
        this.swim(this.N)
    }

    getMax() {
        return this.pq[1]
    }

    delMax() {
        if (this.isEmpty()) {
            console.log('pq is empty')
            return
        }
        let maxItem = this.getMax()
        this.swap(1, this.N--)
        this.pq[this.N + 1] = null  // prevent loitering
        this.sink(1)
        return maxItem
    }

    swim(i) {
        // while child > parent
        while (i > 1 && this.pq[i] > this.pq[Math.floor(i/2)]) {
            this.swap(i, Math.floor(i/2))  // swap parent and child
            i = Math.floor(i/2)  // swim up tree
        }
    }

    sink(i) {
        while (2*i <= this.N) {
            let j = 2*i  // left child index
            if (j < this.N && this.pq[j] < this.pq[j + 1]) j++  
            if (this.pq[i] < this.pq[j]) { // swap parent if smaller than child
                this.swap(i, j)
                i = j
            } else {
                break
            }
        }
    }

    swap(i, j) {
        let temp = this.pq[i]
        this.pq[i] = this.pq[j]
        this.pq[j] = temp
    }
}

/* Test Client */
function main() {
    fs.readFile(__dirname + '/Tests/' + process.argv[2], 'utf8', (err, data) => {
        if (err) throw err
        const commands = data.split('\n')
        const maxPQ = new MaxPQ(Number(commands[0]))
        for (let i = 1; i < commands.length; i++) {
            let cm = commands[i]
            if (cm === 'pop') {
                console.log('max item:', maxPQ.delMax())
            } else {
                maxPQ.insert(Number(cm))
            }
        }
        const sortedArr = new Array(maxPQ.N)
        let range = maxPQ.N
        for (let j = 0; j < range; j++) {
            sortedArr[j] = maxPQ.delMax()
        }
        console.log(sortedArr)
    })
}


main()