# Problem:
# Reverse an array in place using no extra memory in O(N) time

def reverse_array(arr):
    i = 0  # Pointer to beginning of array
    j = len(arr) - 1  # Pointer to end of array
    while i < j:
        # The pythonic way of swapping
        arr[i], arr[j] = arr[j], arr[i]
        i += 1  # Move i forward 1 position
        j -= 1  # Move j backward 1 position


def main():
    test1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]  # Odd number of items
    test2 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']  # Even number of items
    reverse_array(test1)
    reverse_array(test2)
    print(test1)
    print(test2)


main()