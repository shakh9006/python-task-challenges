# Source: https://leetcode.com/problems/letter-combinations-of-a-phone-number/

# Title: Letter Combinations of a Phone Number

# Description

"""
Given a string containing digits from 2-9 inclusive,
return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digits to letters (just like on the telephone buttons) is given below.
Note that 1 does not map to any letters.
"""

def letter_combinations(self, digits: str) :
    if not digits:
        return []

    digit_to_letters = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz',
    }

    def backtrack(idx, comb):
        if idx == len(digits):
            res.append(comb[:])
            return

        for letter in digit_to_letters[digits[idx]]:
            backtrack(idx + 1, comb + letter)

    res = []
    backtrack(0, "")

    return res