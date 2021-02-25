// Check if a given string is a palindrome. ex) 'radar' == True, 'owl' == False

function isPalindrome(string) {
    let start = 0
    let end = string.length - 1
    while (start < end) {
        if (string.charAt(start) !== string.charAt(end)) return false
        start++
        end--
    }
    return true
}

const test1 = 'level'
const test2 = 'leveled'
console.log(isPalindrome(test1))
console.log(isPalindrome(test2))
