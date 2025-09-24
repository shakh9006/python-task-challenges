# Source: https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/description/

# Title: Find the Index of the First Occurrence in a String

# Description

"""
Given two strings needle and haystack,
return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
"""


def find_the_index(haystack: str, needle: str) -> int:
    for i in range(0, len(haystack) - len(needle) + 1):
        if haystack[i:i+len(needle)] == needle:
            return i
    return -1