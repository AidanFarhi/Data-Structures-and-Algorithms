/*
Return all the permutations of a given string. (string will be non-repeating)
ex) 'ab' => ['ab', 'ba'] 
*/

function swap(swapString, i, j) {
    const arr = Array.from(swapString)
    const t = arr[i]
    arr[i] = arr[j]
    arr[j] = t
    return arr.join('')
}

function getPermutations(str, l, r) {
    ouput = []
    function recurse(st, l, r) {
        if (l === r) {
            ouput.push(st)
            return
        } else {
            for (let i = l; i < r; i++) {
                const swapped = swap(st, l, i)
                recurse(swapped, l + 1, r)
            }
        }
    }
    recurse(str, l, r)
    return ouput
}

let test = 'abc'
console.log(getPermutations(test, 0, test.length))

