# Here are three different ways to solve this problem

# 1. Classic recursive solution O(2^n)
def fib_recurse(n):
    if n <= 0:
        return 0
    if n == 1:
        return 1
    return fib_recurse(n - 1) + fib_recurse(n - 2)

recurse_test = fib_recurse(8)  # should return => 21
print(recurse_test)

# 2. Using Memoization O(n)
def fib_memo(n):
  memo = [None] * (n + 1)
  return fib_memo_helper(n, memo)

def fib_memo_helper(n, memo):
  if memo[n]:
    return memo[n]
  if n == 1 or n == 2:
    result = 1
  else:
    result = fib_memo_helper(n - 1, memo) + fib_memo_helper(n - 2, memo)
  memo[n] = result
  return result

mem_test = fib_memo(8)
print(mem_test)

# 3. Bottom up approach O(n)
def fib_bot_up(n):
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        arr = [None] * (n + 1)
        arr[1] = 1
        arr[2] = 1
        for i in range(3, n + 1):
            arr[i] = arr[i - 1] + arr[i - 2]
    return arr[n]

bot_up_test = fib_bot_up(8)
print(bot_up_test)
