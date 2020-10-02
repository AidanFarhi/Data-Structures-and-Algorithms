// Reverse and integer

function reverseInteger(integer) {
    let remainder = 0
    let reversed = 0
    while (integer > 0) {
        remainder = integer % 10
        integer = Math.floor(integer / 10)
        reversed = reversed * 10 + remainder
    }
    return reversed
}

let test = 123456789
let result = reverseInteger(test)
console.log(result)
