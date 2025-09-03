# Source: https://leetcode.com/problems/reverse-integer/description/

# Title:  Reverse Integer

# Description

"""
Given a signed 32-bit integer x, return x with its digits reversed.
If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).
"""


def reverse(x):
    sing = 1
    if x < 0:
        sing = -1
        x = x * -1

    result = 0
    while x:
        result = result * 10 + x % 10
        x //= 10

    result *= sing
    if result <= (-2 ** 31) or result >= (2 ** 31 - 1):
        return 0
    return result