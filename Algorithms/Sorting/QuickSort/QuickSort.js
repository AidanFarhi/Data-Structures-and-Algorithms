class QuickSort {

    static sort(arr) {
        QuickSort.sortHelper(arr, 0, arr.length - 1)
    }

    static sortHelper(arr, lo, hi) {
        if (hi <= lo) return
        let p = QuickSort.partition(arr, lo, hi)
        QuickSort.sortHelper(arr, lo, p - 1)
        QuickSort.sortHelper(arr, p + 1, hi)
    }

    static partition(arr, lo, hi) {
        let i = lo
        let j = hi + 1
        while (true) {
            while (arr[lo] > arr[++i]) {
                if (i == hi) break
            }
            while (arr[lo] < arr[--j]) {
                if (j == lo) break
            }
            if (j <= i) break
            QuickSort.swap(arr, i, j)
        }
        QuickSort.swap(arr, lo, j)
        return j
    }

    static swap(arr, x, y) {
        let temp = arr[x]
        arr[x] = arr[y]
        arr[y] = temp
    }

    static test() {
        const test1 = [5, 1, 66, -15, -66, -1, 66, 77, 167, 2555, -777, 2, 7737, -887, 2, 727, 77]
        const test2 = ['B', 'A', 'Y', 'W', 'U', 'E', 'T', 'B', 'B', 'J', 'T', 'Z', 'A']
        QuickSort.sort(test1)
        QuickSort.sort(test2)
        console.log(test1)
        console.log(test2)
    }
}


QuickSort.test()