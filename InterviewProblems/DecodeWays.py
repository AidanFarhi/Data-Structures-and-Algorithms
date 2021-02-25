"""
A message containing letters from A-Z is being encoded to numbers using the following mapping:
'A' -> 1
'B' -> 2
...
'Z' -> 26
Given a non-empty string containing only digits, determine the total number of ways to decode it.
The answer is guaranteed to fit in a 32-bit integer.
"""

# Iterative approach
def docode_ways(st):
    if not st:
        return 0
    
    # initialize and fill dp[] with len == st + 1
    dp = [0 for _ in range(len(st) + 1)] 
    
    # Initialize the first element to 1
    dp[0] = 1

    # If first char of string is 0, then no decode possible
    dp[1] = 1 if st[0] != '0' else 0

    for i in range(2, len(dp)):
        # Check if succesful single digit decode is possible
        if st[i - 1] != '0':
            dp[i] += dp[i - 1]
        
        # Check if succesful two digit decode is possible
        two_dig = int(st[i - 2 : i])
        if two_dig >= 10 and two_dig <= 26:
            dp[i] += dp[i - 2]
    
    # Return the last value
    return dp[-1]

test = '326'
print(docode_ways(test))    
