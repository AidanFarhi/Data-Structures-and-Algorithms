/*
- Selection Sort -

- Running time -
    O(N^2)

- Not stable
- Usually outperforms Bubble Sort
- In place algorithm O(1) memory
- Usefull when auxiliary memory is limited
- Fast for smaller arrays 10-20 items
*/

function selectionSort(arr) {
    for (let i = 0; i < arr.length - 1; i++) {
        let index = i
        for (let j = i + 1; j < arr.length; j++) {
            if (arr[j] < arr[index]) {
                index = j
            }
        }
        if (index !== i) {
            let temp = arr[index]
            arr[index] = arr[i]
            arr[i] = temp
        }
    }
    return arr
}

const test1 = [4, 1, 6, 33, 777, 4, 333, 4, -1, 664]
const test2 = [-44, 3, -63, 22, 656, -14444, 5, 5, 5]

const result1 = selectionSort(test1)
const result2 = selectionSort(test2)

console.log(result1)
console.log(result2)
