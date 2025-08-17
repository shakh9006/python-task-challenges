# Source: https://www.codewars.com/kata/56b5afb4ed1f6d5fb0000991/train/python

# Title: Reverse or rotate?

# Description

"""
The input is a string str of digits. Cut the string into chunks
(a chunk here is a substring of the initial string) of size sz (ignore the last chunk if its size is less than sz).

If the sum of a chunk's digits is divisible by 2, reverse that chunk; otherwise rotate it to the left by one position.
Put together these modified chunks and return the result as a string.
"""


def rev_rot(strng, sz):
    if sz <= 0 or strng == '' or sz > len(strng):
        return ""

    lst = []
    for i in range(0, len(strng), sz):
        chunk = strng[i:i + sz]
        if len(chunk) < sz:
            break
        if sum(int(digit) for digit in chunk) % 2 == 0:
            lst.append(chunk[::-1])
        else:
            lst.append(chunk[1:] + chunk[0])

    return ''.join(lst)