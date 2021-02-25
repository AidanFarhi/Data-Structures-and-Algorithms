/*

The sum of an array is the sum of all the values in that array. 
Your task is to write a function that takes as input an array and outputs the sum of all of its subarrays. 

For example, given [1, 3, 7], you'd output 36, because:

[ ] + [1] + [3] + [7] + [1, 3] + [3, 7] + [1, 3, 7] =
        0 + 1 + 3 + 7 + 4 + 10 + 11 = 36

*/

// O(N^3)
function bruteForceSubSums(arr) {
    let result = 0
    for (let i = 0; i < arr.length; i++) {
        for (let j = i; j < arr.length; j++) {
            for (let k = i; k <= j; k++) {
                result += arr[k]
            }
        }
    }
    return result
}

// O(N^2)
function optimizedBruteForceSubSums(arr) {
    let result = 0
    for (let i = 0; i < arr.length; i++) {
        let sum = 0
        for (let j = i; j < arr.length; j++) {
            sum += arr[j]
            result += sum
        }
    }
    return result
}

// O(N)
function linearSubSums(arr) {
    let result = 0
    for (let i = 0; i < arr.length; i++) {
        result += arr[i] * (i + 1) * (arr.length - i)
    }
    return result
}

// TEST SECTION
const test_arr = [1, 2, 3, 4] // --> 50

const test1 = bruteForceSubSums(test_arr)
const test2 = optimizedBruteForceSubSums(test_arr)
const test3 = linearSubSums(test_arr)

console.log(`
- Results -
--------------------
Brute force: ${test1}
--------------------
Optimized brute force: ${test2}
--------------------
Linear: ${test3}
--------------------
`)