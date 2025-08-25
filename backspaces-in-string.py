# Source: https://www.codewars.com/kata/5727bb0fe81185ae62000ae3/train/python

# Title: Backspaces in string

# Description

"""
Assume "#" is like a backspace in string. This means that string "a#bc#d" actually is "bd"

Your task is to process a string with "#" symbols.
"""

def clean_string(st):
    result = []
    for i in range(0, len(st)):
        s = st[i]
        if s != '#':
            result.append(s)
        elif len(result) > 0:
            result.pop()

    return ''.join(result)
