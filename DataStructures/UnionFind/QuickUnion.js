const fs = require('fs')

class QuickUnion {
    /*
    * Maintain an array of roots. Entry == root | Index == object id
    */
    constructor(size) {
        this.roots = Array(size)
        for (let i = 0; i < size; i++) {
            this.roots[i] = i
        }
    }
    /*
    * If roots are equal, objects are connected | O(N)
    */
    connected(p, q) {
        return this.getRoot(p) === this.getRoot(q)
    }
    /*
    * Set qRoot == pRoot | O(N) worst case
    */
    union(p, q) {
        const pRoot = this.getRoot(p)
        const qRoot = this.getRoot(q)
        this.roots[qRoot] = pRoot
    }
    /*
    * Keep iterating until index == entry, because every object is it's own root
    */
    getRoot(n) {
        while (n != this.roots[n]) {
            n = this.roots[n]
        }
        return n
    }
}

function main() {
    fs.readFile(__dirname + '/Tests/UF10.txt', 'utf8', 
    function(err, data) {
        if (err) throw err
        const commands = data.split('\n')
        const quickUnion = new QuickUnion(Number(commands[0]))
        for (let i = 1; i < commands.length; i++) {
            const p = Number(commands[i][0])
            const q = Number(commands[i][2]) 
            if (quickUnion.connected(p, q)) {
                console.log(`[${p}, ${q}] are already connected.`)
            } else {
                quickUnion.union(p, q)
                console.log(`[${p}, ${q}] are now connected.`)
            }
        }
    })
}

main()
