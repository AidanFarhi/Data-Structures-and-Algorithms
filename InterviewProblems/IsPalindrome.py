# Check if a given string is a palindrome. ex) 'radar' == True, 'owl' == False

def is_palindrome(string):
    start = 0
    end = len(string) - 1
    while start < end:
        if string[start] != string[end]:
            return False
        start += 1
        end -= 1
    return True

test1 = 'level'
test2 = 'leveled'
print(is_palindrome(test1))
print(is_palindrome(test2))
