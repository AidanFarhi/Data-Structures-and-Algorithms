"""
Find all the permutations of a string. (string will not have repeating characters)
ex) 'abc' => ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']
"""

def find_perms(string):
    result = []

    def swap(swap_str, i, j):
        arr = list(swap_str)
        t = arr[i]
        arr[i] = arr[j]
        arr[j] = t
        return ''.join(arr)
    
    def find_perms_recurse(perm_string, l, r):
        if l == r:
            result.append(perm_string)
            return
        else:
            for i in range(l, r):
                swapped = swap(perm_string, l, i)
                find_perms_recurse(swapped, l + 1, r)
    
    find_perms_recurse(string, 0, len(string))
    return result

test = 'ABC'
print(find_perms(test))
