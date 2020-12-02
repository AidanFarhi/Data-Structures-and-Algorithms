/*
- Counting Sort -

- Operates by counting the number of objects that have each distinct
  value key.
- The values have to be non-negative integers
- Only suitable when the variation in keys in not significantly greater 
  than the number of items. 
- It can outperform comparison based sorting algorithms

    | Runtime Complexity   |   Memory Complexity |
          O(N + K)         |         O(K) 
      K == max - min + 1   |   K == max - min + 1
*/

function countingSort(arr) {
    // Initialize count array
    const countArray = Array(Math.max(...arr) - Math.min(...arr) + 1).fill(0)

    // Add counts of each number to countArray
    for (let i = 0; i < arr.length; i++) {
        let num = arr[i] - 1
        countArray[num]++
    }

    // Add sorted order to original array
    let i = 0
    let j = 0
    while (i < arr.length) {
        while (j < countArray.length) {
            if (countArray[j] > 0) {
                let num = j + 1
                let count = countArray[j]
                let k = 0
                while (k < count) {
                    arr[i] = num
                    i += 1
                    k += 1
                }
            }
            j += 1
        }
    }
    return arr
}

const test = [6, 4, 3, 7, 8, 4, 4, 11, 1, 1, 7]
console.log(countingSort(test))
