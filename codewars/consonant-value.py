# Source: https://www.codewars.com/kata/59c633e7dcc4053512000073/train/python

# Title: Consonant value

# Description

"""
Given a lowercase string that has alphabetic characters only and no spaces, return the highest value of consonant substrings.
Consonants are any letters of the alphabet except "aeiou".

We shall assign the following values: a = 1, b = 2, c = 3, .... z = 26.
"""


def letter_position(letter):
    return ord(letter.lower()) - ord('a') + 1


def solve(s):
    vowels = [letter_position(x) for x in 'aeiou']
    positions = [letter_position(x) for x in s]

    result = []
    temp = []

    for x in positions:
        if x in vowels:
            result.append(sum(temp))
            temp = []
        else:
            temp.append(x)

    if temp:
        result.append(sum(temp))
    return max(result)
