/*
Problem:
Reverse an array in place using no extra memory in O(N) time
*/

function reverseArray(arr) {
    let i = 0
    let j = arr.length - 1
    while (i < j) {
        swap(arr, i, j)
        ++i
        --j
    }
}

function swap(arr, i, j) {
    let t = arr[i]
    arr[i] = arr[j]
    arr[j] = t
}

// Test Area
function main() {
    const test1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]              // odd # of items
    const test2 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'] // even # of items
    reverseArray(test1)
    reverseArray(test2)
    console.log(test1)
    console.log(test2)
}

main()