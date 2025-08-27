# Source: https://www.codewars.com/kata/559e708e72d342b0c900007b/train/python

# Title: Even Odd Pattern #1

# Description

"""
Write a function that takes an array / list of numbers and returns a number.
See the examples and try to guess the pattern:
"""

def comp(array1, array2):
    if array1 is None or array2 is None or len(array1) != len(array2): return False

    array1 = sorted([abs(x) for x in array1])
    array2 = sorted(array2)

    result = True
    for i in range(0, len(array1)):
        x = array1[i]
        y = array2[i]
        if (x * x) != y:
            return False

    return result
