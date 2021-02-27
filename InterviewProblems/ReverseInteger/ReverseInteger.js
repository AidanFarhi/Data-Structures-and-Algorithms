/*
Problem:
Reverse a positive integer. 
Can you do it without using an additional data structure (arr, string, ect..)?
ex) 1234 -> 4321
*/

function reverseInt(num) {
    let res = 0
    while (num > 0) {
        let rem = num % 10
        num = Math.floor(num / 10)
        res = res * 10 + rem
    }
    return res
}

function main() {
    console.log(reverseInt(1234))
    console.log(reverseInt(5432))
}

main()