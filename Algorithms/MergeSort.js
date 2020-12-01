/*
- Merge Sort -

- Divide and conquer algorithm
- Comparison Based Algorithm
- A stable sorting algorithm
- Not an in place algorithm
- Usually merge sort is the best option for sorting a linked list

 Runtime Complexity | Memory Complexity 
     O(N logN)              O(N)
*/

function mergeSort(arr) {
    // Base case
    if (arr.length == 1) return

    // Divide
    let mid = Math.floor(arr.length / 2)
    let left = arr.slice(0, mid)
    let right = arr.slice(mid)

    mergeSort(left)
    mergeSort(right)

    // Conquer
    let i = 0
    let j = 0
    let k = 0

    while (i < left.length && j < right.length) {
        if (left[i] < right[j]) {
            arr[k] = left[i]
            i++
        } else {
            arr[k] = right[j]
            j++
        }
        k++
    }

    // If there are remaining elements in the left sub array
    while (i < left.length) {
        arr[k] = left[i]
        i++
        k++
    }

    // If there are remaining elements in the right sub array
    while (j < right.length) {
        arr[k] = right[j]
        j++
        k++
    }
}

const test = [-53, 22, 644, 3, 1, 1, 1, 455, -45, -22, -64, 2, 77]
mergeSort(test)
console.log(test)
