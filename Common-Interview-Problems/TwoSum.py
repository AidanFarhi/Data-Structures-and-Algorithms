"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

"""

test = [7,15,11,2]
target = 9

# Brute force approach - 
# O(N ** 2) Time, 
# O(1) Space

def two_sum(arr, targ):
  for i in range(len(arr)):
    for j in range(i + 1, len(arr)):
      if arr[i] + arr[j] == targ:
        return [i, j]


print('Brute force:', two_sum(test, target))

# Approach with hash map two passes 
# O(N) Time 
# O(N) space

def two_sum_two_pass(arr, target):
  mp = {}
  for i, num in enumerate(arr):
    mp[num] = i
  for i in range(len(arr)):
    comp = target - arr[i]
    if comp in mp:
      return [i, mp[comp]]
  return []


print('Two pass hashmap:', two_sum_two_pass(test, target))

# Approach with hash map with one pass 
# O(N) Time 
# O(N) space

def two_sum_one_pass(arr, target):
  mp = {}
  for i, num in enumerate(arr):
    comp = target - num
    if comp in mp:
      return [mp[comp], i]
    else:
      mp[num] = i

print('One pass hashmap:', two_sum_one_pass(test, target))
