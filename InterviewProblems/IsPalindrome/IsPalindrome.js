/*
Problem:
Check if a string is a palindrome or not.
Ex) is_palindrome(level) -> True | is_palindrome(levels) -> False
*/

function isPalindrome(str) {
    let i = 0
    let j = str.length - 1
    while (i <= j) {
        if (str[i] != str[j]) return false
        ++i
        --j
    }
    return true
}

function main() {
    const test1 = 'level'
    const test2 = 'levels'
    console.log('level:', isPalindrome(test1))
    console.log('levels:', isPalindrome(test2))
}

main()