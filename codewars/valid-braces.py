# Source: https://www.codewars.com/kata/5277c8a221e209d3f6000b56/train/python

# Title: Valid Braces

# Description

# Write a function that takes a string of braces, and determines if the order of the braces is valid.
# It should return true if the string is valid, and false if it's invalid.
#
# This Kata is similar to the Valid Parentheses Kata,
# but introduces new characters: brackets [], and curly braces {}. Thanks to @arnedag for the idea!
#
# All input strings will be nonempty, and will only consist of parentheses, brackets and curly braces: ()[]{}.

def valid_braces(string: str) -> bool:
    stack = []
    matching = {')': '(', ']': '[', '}': '{'}

    for char in string:
        if char in matching.values():
            stack.append(char)
        elif char in matching:
            if not stack or stack[-1] != matching[char]:
                return False
            stack.pop()

    return not stack

