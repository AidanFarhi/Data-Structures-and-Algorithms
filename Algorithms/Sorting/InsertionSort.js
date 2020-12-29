/*
- Insertion Sort -

| Running Time |
    O(N^2)

- Efficient on smaller data sets 10-20 items
- More efficient than Bubble Sort and Selection Sort
- Speeds up when array is already partially sorted
- Stable Algorithm (preserves original order of elements)
- In place algorithm
- In general, insertion sort will write to an array O(N^2) times,
  while selection sort will only write O(N) times. (selection better for flash memory)
*/

function insertionSort(arr) {
    for (let i = 0; i < arr.length; i++) {
        let j = i
        while (j > 0 && arr[j - 1] > arr[j]) {
            let temp = arr[j]
            arr[j] = arr[j - 1]
            arr[j - 1] = temp
            j--
        }
    }
    return arr
}

const test1 = [4, 1, 6, 33, 777, 4, 333, 4, -1, 664]
const test2 = [-44, 3, -63, 22, 656, -14444, 5, 5, 5]

const result1 = insertionSort(test1)
const result2 = insertionSort(test2)

console.log(result1)
console.log(result2)
