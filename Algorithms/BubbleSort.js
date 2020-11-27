/*

- Bubble Sort -

Iterate through the array, compare each pair of adjacent items,
and swap them if they are in the wrong order.

- Worst Case Running Time: O(n^2)
- Stable (Maintains relative order of elements)
- In place (No extra memory)

*/

function bubbleSort(arr) {
    for (let i = 0; i < arr.length - 1; i++) {
        for (let j = 0; j < arr.length - 1 - i; j++) {
            if (arr[j] > arr[j + 1]) {
                let temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp
            }
        }
    }
}

const test = [-2, 5, 2, -66, 23, -6, 144, 36]
bubbleSort(test)
console.log(test)
