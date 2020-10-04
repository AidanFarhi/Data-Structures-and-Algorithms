/* 
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order 
*/

const test = [7,15,11,2]
const target = 9

// Brute Force Approach

function twoSumBruteForce(arr, target) {
    for (let i = 0; i < arr.length; i++) {
        for (let j = i + 1; j < arr.length; j++) {
            if (arr[i] + arr[j] === target) {
                return [i, j]
            }
        }
    }
}

console.log('Brute Force:', twoSumBruteForce(test, target))

function twoSumTwoPassHash(arr, target) {
    const mp = new Map()
    for (let i = 0; i < arr.length; i++) {
        mp.set(arr[i], i)
    }
    for (let i = 0; i < arr.length; i++) {
        const comp = target - arr[i]
        if (mp.has(comp) && mp.get(comp) !== i) {
            return [i, mp.get(comp)]
        }
    }
}

console.log('Hash Map Two Pass:', twoSumTwoPassHash(test, target))

function twoSumOnePassHash(arr, target) {
    const mp = new Map()
    for (let i = 0; i < arr.length; i++) {
        const comp = target - arr[i]
        if (mp.has(comp)) return [mp.get(comp), i]
        mp.set(arr[i], i)
    }
}

console.log('Hash Map One Pass:', twoSumOnePassHash(test, target))
