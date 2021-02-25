/*
Given a sorted array nums, remove the duplicates in-place such that each element 
appears only once and returns the new length.
Do not allocate extra space for another array, 
you must do this by modifying the input array in-place with O(1) extra memory.
*/

function removeDuplicates(arr) {
    let i = 1
    for (let n = 1; n < arr.length; n++) {
        if (arr[n] !== arr[n - 1]) {
            arr[i] = arr[n]
            i++
        }
    }
    return i
}
