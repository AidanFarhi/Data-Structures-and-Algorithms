
class SelectionSort {

    static sort(arr) {
        const N = arr.length;
        for (let i = 0; i < N; i++) {
            let min = i
            for (let j = i + 1; j < N; j++) {
                if (arr[j] < arr[min]) {
                    min = j
                }
            }
            SelectionSort.swap(arr, i, min)
        }
    }

    static swap(arr, i, j) {
        const temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp
    }
}

const test1 = ["B", "C", "X", "A", "P"]
const test2 = [5, -11, 555, -61, 636, -99]

SelectionSort.sort(test1)
SelectionSort.sort(test2)

console.log(test1)
console.log(test2)
