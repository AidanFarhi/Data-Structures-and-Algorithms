"""
Given a 32-bit signed integer, reverse digits of an integer.
Note:
Assume we are dealing with an environment that could only store integers within the 32-bit signed integer range: 
[−231,  231 − 1]. 
For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
"""

def reverse_integer(x):
    neg_check = False
    if x < 0:
        neg_check = True
        x = abs(x)
    rem = 0
    rev = 0
    while x > 0:
        rem = x % 10
        x = x // 10
        rev = rev * 10 + rem
    if neg_check:
        rev = -rev
        if rev < -2 ** 31:
            return 0
        else:
            return rev
    elif rev > 2 ** 31:
        return 0
    else:
        return rev

test1 = 123456789
test2 = -987654321
test3 = 12345670889345938495
test4 = -1234560230342342

rev1 = reverse_integer(test1)
print(rev1)
rev2 = reverse_integer(test2)
print(rev2)
rev3 = reverse_integer(test3)
print(rev3)
rev4 = reverse_integer(test4)
print(rev4)
