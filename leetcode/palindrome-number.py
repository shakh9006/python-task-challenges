# Source: https://leetcode.com/problems/palindrome-number/description/

# Title: Palindrome Number

# Description

"""
Given an integer x, return true if x is a palindrome, and false otherwise.
"""


def is_palindrome(x: int) -> bool:
    return str(x) == str(x)[::-1]