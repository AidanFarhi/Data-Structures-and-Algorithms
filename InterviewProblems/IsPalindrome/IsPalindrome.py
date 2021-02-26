# Problem:
# Check if a string is a palindrome or not.
# Ex) is_palindrome(level) -> True | is_palindrome(levels) -> False

def is_palindrome(string):
    i = 0
    j = len(string) - 1
    while i <= j:
        if string[i] != string[j]:
            return False
        i += 1
        j -= 1
    return True


def main():
    test1 = 'level'
    test2 = 'levels'
    print('level:', is_palindrome(test1))
    print('levels:', is_palindrome(test2))


main()