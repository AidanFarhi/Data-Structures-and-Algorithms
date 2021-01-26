
class InsertionSort {

    static sort(arr) {
        const N = arr.length
        for (let i = 0; i < N; i++) {
            for (let j = i; j > 0; j--) {
                if (arr[j] < arr[j - 1]) {
                    InsertionSort.swap(arr, j, j - 1)
                } else {
                    break
                }
            }
        }
    }

    static swap(arr, i, j) {
        const temp = arr[i];
        arr[i] = arr[j]
        arr[j] = temp
    }
}

const test1 = ["B", "C", "X", "A", "P"]
const test2 = [5, -11, 555, -61, 636, -99]

InsertionSort.sort(test1)
InsertionSort.sort(test2)

console.log(test1)
console.log(test2)