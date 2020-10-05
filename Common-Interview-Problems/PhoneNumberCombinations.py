"""
Problem:
Given a string containing digits from 2-9 inclusive, 
return all possible letter combinations that the number could represent. 
Return the answer in any order.
Note that 1 does not map to any letters.

Time:
O(4^n) * O(1) * O(n) = O(n(4^n)) [weak upper bound]
Since there are no more than 4 possible characters for each digit, there will be O(4^n) function calls at max.
Each call of the function will make at max 4 more calls. 4 * 4 * 4 * 4 * 4... = 4^n, 
n being the amount of digits provided as input.
O(1) work in each function call for the most part
O(n) time to copy the string over to the answer list in each base case since that is done character by character.

Space:
O(n) + O(4^n) = O(4^n)
Our recursion tree will go at max n calls deep.
We will have at max 4 choices at each digits so total we have roughly 3^n or 4^n
total mneumonics that pan out and get stored in the result array.
"""

def number_combinations(ph_number_string):
    if not ph_number_string or len(ph_number_string) == 0:
        return []
    current = ''
    result_combos = []
    number_combo_helper(ph_number_string, 0, result_combos, current)
    return result_combos

def number_combo_helper(ph_n_str, index, r_comb, current):
    if index == len(ph_n_str):
        r_comb.append(current)
    else:
        letters = mapper(ph_n_str[index])
        for i in range(len(letters)):
            char = letters[i]
            number_combo_helper(ph_n_str, index + 1, r_comb, current + char)            

def mapper(number_char):
    phone_mapping = [
        '0',
        '1',
        'ABC',
        'DEF',
        'GHI',
        'JKL',
        'MNO',
        'PQRS',
        'TUV',
        'WXYZ'
    ]
    return phone_mapping[int(number_char)]

test = '23'
print(number_combinations(test))
