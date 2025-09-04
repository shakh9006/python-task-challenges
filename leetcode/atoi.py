# Source: https://leetcode.com/problems/string-to-integer-atoi/description/

# Title: String to Integer (atoi)

# Description

"""
Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer.

The algorithm for myAtoi(string s) is as follows:

1. Whitespace: Ignore any leading whitespace (" ").

2. Signedness: Determine the sign by checking if the next character is '-' or '+', assuming positivity if neither present.

3. Conversion: Read the integer by skipping leading zeros until a non-digit character is encountered or the end of the string is reached. If no digits were read, then the result is 0.

4. Rounding: If the integer is out of the 32-bit signed integer range [-231, 231 - 1], then round the integer to remain in the range. Specifically, integers less than -231 should be rounded to -231, and integers greater than 231 - 1 should be rounded to 231 - 1.
Return the integer as the final result.


"""


def my_atoi(s):
    INT_MAX, INT_MIN = 2 ** 31 - 1, -2 ** 31
    i, n = 0, len(s)
    while i < n and s[i] == ' ':
        i += 1

    sign = 1
    if i < n and s[i] == '-':
        sign = -1
        i += 1
    elif i < n and s[i] == '+':
        i += 1

    result = 0
    while i < n and s[i].isdigit():
        digit = int(s[i])
        if result > (INT_MAX - digit) // 10:
            return INT_MAX if sign == 1 else INT_MIN
        result = result * 10 + digit
        i += 1

    return sign * result