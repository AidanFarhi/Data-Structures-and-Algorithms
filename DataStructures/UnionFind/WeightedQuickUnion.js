const fs = require('fs')

class WeightedQuickUnion {
    // The same as QuickUnion, except we maintain an array of sizes
    constructor(size) {
        this.roots = Array(size)
        this.sizes = Array(size)
        for (let i = 0; i < size; i++) {
            this.roots[i] = i;
            this.sizes[i] = 1;
        }
    }

    connected(p, q) {
        return this.getRoot(p) === this.getRoot(q)
    }

    getRoot(n) {
        while (n != this.roots[n]) {
            this.roots[n] = this.roots[this.roots[n]] // Path compression
            n = this.roots[n]
        }
        return n
    }

    union(p, q) {
        const pRoot = this.getRoot(p)
        const qRoot = this.getRoot(q)
        if (pRoot !== qRoot) {
            if (this.sizes[pRoot] < this.sizes[qRoot]) {
                this.roots[pRoot] = qRoot
                this.sizes[qRoot]++
            } else {
                this.roots[qRoot] = pRoot
                this.sizes[pRoot]++
            }
        }
    }
}

function main() {
    fs.readFile(__dirname + '/Tests/UF10.txt', 'utf8', 
    function(err, data) {
        if (err) throw err
        const commands = data.split('\n')
        const weightedQuickUnion = new WeightedQuickUnion(Number(commands[0]))
        for (let i = 1; i < commands.length; i++) {
            const p = Number(commands[i][0])
            const q = Number(commands[i][2]) 
            if (weightedQuickUnion.connected(p, q)) {
                console.log(`[${p}, ${q}] are already connected.`)
            } else {
                weightedQuickUnion.union(p, q)
                console.log(`[${p}, ${q}] are now connected.`)
            }
        }
    })
}

main()
