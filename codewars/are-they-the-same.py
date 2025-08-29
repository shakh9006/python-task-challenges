# Source: https://www.codewars.com/kata/550498447451fbbd7600041c/train/python

# Title: Are they the "same"?

# Description

"""
Given two arrays a and b write a function comp(a, b) (orcompSame(a, b)) that checks whether the two arrays have the "same"
elements, with the same multiplicities (the multiplicity of a member is the number of times it appears).
"Same" means, here, that the elements in b are the elements in a squared, regardless of the order.
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
