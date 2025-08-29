# Source: https://www.codewars.com/kata/5546180ca783b6d2d5000062/train/python

"""
Description

Complete the function that returns an array of length n, starting with the given number x and the squares of the previous number.
If n is negative or zero, return an empty array/list.

"""


def squares(x, n):
    if n <= 0: return []

    result = [x]
    for i in range(1, n):
        result.append(pow(result[-1], 2))

    return result