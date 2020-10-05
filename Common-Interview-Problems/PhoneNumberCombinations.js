/*
Problem:
Given a string containing digits from 2-9 inclusive, 
return all possible letter combinations that the number could represent. 
Return the answer in any order.
Note that 1 does not map to any letters.

Time:
O(4^n) * O(1) * O(n) = O(n(4^n)) [weak upper bound]
Since there are no more than 4 possible characters for each digit, there will be O(4^n) function calls at max.
Each call of the function will make at max 4 more calls. 4 * 4 * 4 * 4 * 4... = 4^n, 
n being the amount of digits provided as input.
O(1) work in each function call for the most part
O(n) time to copy the string over to the answer list in each base case since that is done character by character.

Space:
O(n) + O(4^n) = O(4^n)
Our recursion tree will go at max n calls deep.
We will have at max 4 choices at each digits so total we have roughly 3^n or 4^n
total mneumonics that pan out and get stored in the result array.
*/

function getCombos(digits) {
    const result = []
    let current = ''
    getCombosHelper(digits, result, current, 0)
    return result
}

function getCombosHelper(dig, res, cur, ind) {
    if (ind == dig.length) {
        res.push(cur)
        return
    } else {
        const letters = mapper(dig.charAt(ind))
        for (let i = 0; i < letters.length; i++) {
            const ch = letters.charAt(i)
            getCombosHelper(dig, res, cur + ch, ind + 1)
        }
    }
}

function mapper(dig) {
    mp = [
        '0',
        '1',
        'abc',
        'def',
        'ghi',
        'jkl',
        'mno',
        'pqrs',
        'tuv',
        'wxyz'
    ]
    return mp[Number(dig)]
}

let test = '23'
console.log(getCombos(test))
