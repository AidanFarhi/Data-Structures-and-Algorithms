# Given an array of integers, 
# find the contiguous subarray (containing at least one number) 
# which has the largest sum and return its sum.

# Kadanes Algorithm: O(N) time complexity 
def kadanes_algorithm(arr):
    max_global = arr[0]
    max_current = arr[0]
    for i in range(1, len(arr)):
        max_current = max(arr[i], max_current + arr[i])
        if max_current > max_global:
            max_global = max_current
    return max_global
