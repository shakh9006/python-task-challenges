# Source: https://leetcode.com/problems/valid-parentheses/description/

# Title: Valid Parentheses

# Description

"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
"""


def is_valid(s: str) -> bool:
    chars = {
        ')': '(',
        '}': '{',
        ']': '['
    }

    temp = []
    for ch in s:
        if ch in chars:
            if len(temp) == 0 or chars[ch] != temp[-1]:
                return False

            temp.pop()
        else:
            temp.append(ch)

    return len(temp) == 0