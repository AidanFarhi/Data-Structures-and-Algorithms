"""

The sum of an array is the sum of all the values in that array. 
Your task is to write a function that takes as input an array and outputs the sum of all of its subarrays. 

For example, given [1, 3, 7], you'd output 36, because:

[ ] + [1] + [3] + [7] + [1, 3] + [3, 7] + [1, 3, 7] =
        0 + 1 + 3 + 7 + 4 + 10 + 11 = 36

"""

# O(N^3)
def brute_force_sub_sums(arr):
    result = 0
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            for k in range(i, j + 1):
                result += arr[k]
    return result

# O(N^2)
def optimized_brute_force_sub_sums(arr):
    result = 0
    for i in range(len(arr)):
        sum = 0
        for j in range(i, len(arr)):
            sum += arr[j]
            result += sum
    return result

# O(N)
# The approach here is to mathematically count all
# the occurances of each item of the array. 
# The formula is: (n – i)(i + 1)
def linear_sub_sums(arr):
    result = 0
    for i in range(len(arr)):
        result += arr[i] * (i + 1) * (len(arr) - i)
    return result

# TEST SECTION
test_arr = [1, 2, 3, 4] # --> 50

test1 = brute_force_sub_sums(test_arr)
test2 = optimized_brute_force_sub_sums(test_arr)
test3 = linear_sub_sums(test_arr)

print(f'''
- Results -
--------------------
Brute force: {test1}
--------------------
Optimized brute force: {test2}
--------------------
Linear: {test3}
--------------------
''')
