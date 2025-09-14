# Source: https://leetcode.com/problems/integer-to-roman/description/

# Title: Integer to Roman

# Description

"""
Seven different symbols represent Roman numerals with the following values:

I	1
V	5
X	10
L	50
C	100
D	500
M	1000
"""

def int_to_roman(num: int) -> str:
    num_map = {
        1: "I",
        5: "V",
        4: "IV",
        9: "IX",
        10: "X",
        40: "XL",
        50: "L",
        90: "XC",
        100: "C",
        400: "CD",
        500: "D",
        900: "CM",
        1000: "M",
    }

    r = ''
    nums = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    for n in nums:
        while n <= num:
            r += num_map[n]
            num -= n
    return r