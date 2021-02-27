# Problem:
# Reverse an given positive integer. 
# Can you do it without using an additional data structure (list, string, ect..)?
# ex) 1234 -> 4321

# Solution without an array
def reverse_integer(number):
    res = 0
    while number > 0:
        rem = number % 10
        number = number // 10
        res = res * 10 + rem
    return res


def main():
    print(reverse_integer(1234))
    print(reverse_integer(5432))
    print(reverse_integer(10013))


main()