# Reverse a given integer

def reverse_integer(integer):
    reversed = 0
    remainder = 0
    while integer > 0:
        remainder = integer % 10
        integer = integer // 10
        reversed = reversed * 10 + remainder
    return reversed

test = 123456789
rev = reverse_integer(test)
print(rev)
