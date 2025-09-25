# Source: https://leetcode.com/problems/divide-two-integers/description/

# Title: Divide Two Integers

# Description

"""
Given two integers dividend and divisor,
 divide two integers without using multiplication, division, and mod operator.
"""
import math

def divide(dividend: int, divisor: int) -> int:
    res = math.trunc(dividend / divisor)
    if res > pow(2, 31) - 1:
        return pow(2, 31) - 1

    return res