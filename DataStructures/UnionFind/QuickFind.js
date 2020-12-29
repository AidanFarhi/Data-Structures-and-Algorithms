const fs = require('fs')

class QuickFind {
    /*
    * Maintain an integer array of size N where N == number of objects.
    * Index == Object id | Array entry == Root
    * If two objects have the same root, they are connected.
    */
    constructor(size) {
        this.roots = new Array(size)
        for (let i = 0; i < size; i++) { // Set each object's root to itself
            this.roots[i] = i
        }
    }

    /*
    * Check if two objects are connected
    * O(1)
    */
    connected(p, q) {
        return this.roots[p] === this.roots[q]
    }

    /*
    * To connect two objects, we change all entries of root[q] to equal root[p]
    * O(N)
    */
   union(p, q) {
       if (!this.connected(p, q)) {
           const pRoot = this.roots[p]
           const qRoot = this.roots[q]
           for (let i = 0; i < this.roots.length; i++) {
               if (this.roots[i] == qRoot) {
                   this.roots[i] = pRoot
               }
           }
       }
   }
}

/*
*   Test Section: 
* - Read in pairs of integers from standard input. 
* - If they are not yet connected, connect them and print out pair
*/
function main() {
    fs.readFile(__dirname + '/Tests/UF10.txt', 'utf8', 
    function(err, data) {
        if (err) throw err
        const commands = data.split('\n')
        const quickFind = new QuickFind(Number(commands[0]))
        for (let i = 1; i < commands.length; i++) {
            const p = Number(commands[i][0])
            const q = Number(commands[i][2]) 
            if (quickFind.connected(p, q)) {
                console.log(`[${p}, ${q}] are already connected.`)
            } else {
                quickFind.union(p, q)
                console.log(`[${p}, ${q}] are now connected.`)
            }
        }
    })
}

main()
