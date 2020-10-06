"""
Write an algorithm to determine if a number n is "happy".
A happy number is a number defined by the following process: 
Starting with any positive integer, replace the number by the sum of the squares of its digits, 
and repeat the process until the number equals 1 (where it will stay), 
or it loops endlessly in a cycle which does not include 1. 
Those numbers for which this process ends in 1 are happy numbers.

Return True if n is a happy number, and False if not.

Example: 

Input: 19
Output: true
Explanation: 
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1
"""

# Maintain a dict with seen values. 
# If num is not a happy number,
# it will pop up again in the loop.

def happy_number(n):
    seen = {}
    prev = 0
    while True:
        last = n
        st = n(st)
        squared = 0
        for i in st:
            squared += int(i) ** 2
        if squared == 1:
            return True
        elif squared in seen:
            return False
        else:
            seen[last] = last
            n = squared
