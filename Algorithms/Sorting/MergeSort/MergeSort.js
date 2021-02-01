class MergeSort {

    static sort(arr) {
        const aux = arr.slice()
        MergeSort.sortHelper(arr, aux, 0, arr.length - 1)
    }

    static sortHelper(arr, aux, lo, hi) {
        if (hi <= lo) return
        const mid = Math.floor(lo + (hi - lo) / 2)
        MergeSort.sortHelper(arr, aux, lo, mid)
        MergeSort.sortHelper(arr, aux, mid + 1, hi)
        MergeSort.merge(arr, aux, lo, mid, hi)
    }

    static merge(arr, aux, lo, mid, hi) {
        for (let n = lo; n <= hi; n++) {
            aux[n] = arr[n]
        }
        let i = lo
        let j = mid + 1
        for (let k = lo; k <= hi; k++) {
            if (i > mid) {
                arr[k] = aux[j]
                j++
            } else if (j > hi) {
                arr[k] = aux[i]
                i++
            } else if (aux[i] < aux[j]) {
                arr[k] = aux[i]
                i++
            } else {
                arr[k] = aux[j]
                j++
            }
        }
    }

    static main() {
        const test1 = [6, -1, 66, -166, 616, -7, 167, 71, 4, -11, 522, 7377, -444, 626, 777, 11111, -72727]
        const test2 = ["Jack", "Alice", "Bob", "Jill", "Sue", "Fred", "Lue", "Zippy", "Scooter", "Lucy"]
        MergeSort.sort(test1)
        MergeSort.sort(test2)
        console.log(test1)
        console.log(test2)
    }
}

MergeSort.main()