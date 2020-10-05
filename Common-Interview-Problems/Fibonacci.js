// Fibonacci three ways

// 1. Classic recursive solution 0(2^n)
function fibRecurse(n) {
    if (n === 0) return 0
    if (n == 1 || n == 2) return 1
    return fibRecurse(n - 1) + fibRecurse(n - 2)
}

const fibTest = fibRecurse(8)
console.log(fibTest)

// 2. Memoization solution
function fibMem(n) {
    const memo = Array(n + 1).fill(null)
    return fibMemHelper(n, memo)
}
function fibMemHelper(n, memo) {
    if (memo[n]) {
        return memo[n]
    }
    if (n == 1 || n == 2) {
        result = 1
    } else {
        result = fibMemHelper(n - 1, memo) + fibMemHelper(n - 2, memo)
        memo[n] = result
    }
    return result
}

const memTest = fibMem(8)
console.log(memTest)

// 3. Bottom up approach O(n)
// (Most intuitive in my opinion.)
function fibBotUp(n) {
    if (n === 0) return 0
    if (n == 1 || n == 2) return 1
    arr = Array(n + 1).fill(null)
    arr[1] = 1
    arr[2] = 1
    for (i = 3; i < n + 1; i++) {
        arr[i] = arr[i - 1] + arr[i - 2]
    }
    return arr[n]
}

const bottUpTest = fibBotUp(8)
console.log(bottUpTest)
