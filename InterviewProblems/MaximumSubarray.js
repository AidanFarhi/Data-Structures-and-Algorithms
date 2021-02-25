/*
Given an array of integers, 
find the contiguous subarray (containing at least one number) 
which has the largest sum and return its sum.
*/

// Kadanes Algorithm: O(N) time complexity O(1) space
function kadanesAlgorithm(arr) {
    let currentMax = arr[0]
    let globalMax = arr[0]
    for (let i = 1; i < arr.length; i++) {
        currentMax = Math.max(arr[i], currentMax + arr[i])
        if (currentMax > globalMax) {
            globalMax = currentMax
        }
    }
    return globalMax
}
