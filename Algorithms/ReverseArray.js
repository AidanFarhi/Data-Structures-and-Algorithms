// Reverse an array without using extra memory

function reverseArray(arr) {
    let start = 0
    let end = arr.length - 1
    while (start < end) {
        let t = arr[start]
        arr[start] = arr[end]
        arr[end] = t
        start++
        end--
    }
}

const test = [1, 2, 3, 4, 5, 6, 7, 8, 9]
reverseArray(test)
console.log(test)
