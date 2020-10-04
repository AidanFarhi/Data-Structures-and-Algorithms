
function getPermutations(arr) {
    const output = []
    function swap(arrToSwap, i, j) {
        const t = arrToSwap[i]
        arrToSwap[i] = arrToSwap[j]
        arrToSwap[j] = t
    }
    function generate(len, heapArr) {
        if (len === 1) {
            output.push(heapArr.slice())
            return
        }
        generate(len - 1, heapArr) 
        for (let i = 0; i < len - 1; i++) {
            if (len % 2 == 0) {
                swap(heapArr, i, len - 1)
            } else {
                swap(heapArr, 0, len - 1)
            }
            generate(len - 1, heapArr)
        }
    }
    generate(arr.length, arr.slice())
    return output
}

const test = [1,2,3]
console.log(getPermutations(test))
