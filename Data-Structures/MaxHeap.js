/*
- Heap -

- It is complete: it cannot be unbalanced. We insert every new item to the next available place
- The heap is one maximally efficient implementation of a priority queue abstract data type
- It has nothing to do with the pool of memory from which dynamically allocated memory is allocated

- Basically a binary tree
- Either min heap or max heap
- Constructed from left to right

Min Heap:
- Parent nodes are always less then or equal to child nodes
- Lowest node is the root
Max Heap:
- Parent nodes are always more than or equal to child nodes
- Highest node is the root

Applications:

- Dijkstra's algorithm, Prims algorithm
*/

class MaxHeap {
    constructor(capacity) {
        this.capacity = capacity
        this.heap = Array(capacity).fill(null)
        this.size = 0
    }
    insert(item) {
        if (this.capacity === this.size){
            return
        }
        this.heap[this.size] = item
        this.size++
        this.fixUp(this.size - 1)
    }
    fixUp(index) {
        let pIndex = Math.floor((index - 1) / 2)
        if (index > 0 && this.heap[pIndex] < this.heap[index]) {
            this.swap(pIndex, index)
            this.fixUp(pIndex)
        }
    }
    swap(i, j) {
        let swap = this.heap[i]
        this.heap[i] = this.heap[j]
        this.heap[j] = swap
    }
    poll() {
        const data = this.heap[0]
        this.swap(0, this.size - 1)
        this.size--
        this.fixDown(0)
        return data
    }
    fixDown(index) {
        let leftIndex = index * 2 + 1
        let rightIndex = index * 2 + 2
        let maxIndex = index
        if (leftIndex < this.size && this.heap[leftIndex] > this.heap[maxIndex]) {
            maxIndex = leftIndex
        }
        if (rightIndex < this.size && this.heap[rightIndex] > this.heap[maxIndex]) {
            maxIndex = rightIndex
        }
        if (maxIndex !== index) {
            this.swap(index, maxIndex)
            this.fixDown(maxIndex)
        }
    }
    heapSort() {
        const range = this.size
        for (i = 0; i < range; i++) {
            this.poll()
        }
    }
}

const heap = new MaxHeap(10)
const arr = [10, 8, 12, 20, -2, 0, 1, 321, 44, 55]
for (i = 0; i < arr.length; i++) {
    heap.insert(arr[i])
}

heap.heapSort()
console.log(heap.heap)
console.log(heap.size)
