class HeapSort {

    static sort(arr) {
        let N = arr.length - 1
        HeapSort.heapify(arr, N) // O(N)
        while (N > 0) { // O(logN)
            HeapSort.swap(arr, 0, N)
            HeapSort.sink(arr, 0, --N)
        }
    }

    static heapify(arr, N) {
        // N/2 because right half of arr are all subtrees of size 1
        for (let i = Math.floor(N/2); i >= 0; i--) {
            HeapSort.sink(arr, i, N)
        }
    }

    static sink(arr, i, N) {
        while (i*2 <= N) {
            let j = i*2  // left child
            if (j < N && arr[j] < arr[j + 1]) j++  // find larger child
            if (arr[i] < arr[j]) {
                HeapSort.swap(arr, i, j)
                i = j
            } else {
                break
            }
        }
    }

    static swap(arr, i, j) {
        let t = arr[i]
        arr[i] = arr[j]
        arr[j] = t
    }
}


function main() {
    const test1 = [5, 1, -66, 141, 667, -567, 1, 777, 2, 1, -88, 2, 6, 7, 7, -222, 7, 22]
    const test2 = ["J", "Y", "B", "N", "Q", "P", "A", "R", "H", "G", "Y", "W", "U", "Z", "K"]
    HeapSort.sort(test1)
    HeapSort.sort(test2)
    console.log(test1)
    console.log(test2)
}


main()