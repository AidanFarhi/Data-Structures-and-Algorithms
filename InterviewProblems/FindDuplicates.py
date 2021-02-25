# Find duplicates in an array in O(N) time in place (no extra memory)

def find_duplicates(arr):
    return len(arr) != len(set(arr))

test = [1, 2, 3, 4, 5]
print(find_duplicates(test))
