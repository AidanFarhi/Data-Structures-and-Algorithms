/*
        - Quick Sort -

    - Running Time Complexity -

  | -Best Case- | -Worst Case- |
    O(N logN)       O(N^2)

- In place O(1) memory
- Not a stable algorithm (Does not maintain original order)
- Widely used in programming languages
- Primitive types - Usually are used with quicksort
- Reference types or objects - Usually used with mergesort
*/

function quickSort(arr, low, high) {
    if (low >= high) return
    let pivot = partition(arr, low, high)
    quickSort(arr, pivot + 1, high)
    quickSort(arr, low, pivot - 1)
}

function partition(arr, low, high) {
    let mid = Math.floor((low + high) / 2)
    swap(arr, mid, high)
    let i = low
    for (let j = low; j < high; j++) {
        if (arr[j] <= arr[high]) {
            swap(arr, j, i)
            i++
        }
    }
    swap(arr, i, high)
    return i
}

function swap(arr, i, j) {
    let temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp
}

const test1 = [4, 1, 6, 33, 777, 4, 333, 4, -1, 664]
const test2 = [-44, 3, -63, 22, 656, -14444, 5, 5, 5]
const test3 = [-54, 34, 5, -5, 0, 44, 1414, 6, 6, 343]

quickSort(test1, 0, test1.length - 1)
quickSort(test2, 0, test2.length - 1)
quickSort(test3, 0, test3.length - 1)

console.log(test1)
console.log(test2)
console.log(test3)
