# Source: https://leetcode.com/problems/longest-substring-without-repeating-characters/description/

# Title: Longest Substring Without Repeating Characters

# Description

"""
Given a string s, find the length of the longest substring without duplicate characters.
"""

def length_of_longest_substring(s):
    seen_counter = 0
    seen = set()
    max_len = 0

    for i, ch in enumerate(s):
        while ch in seen:
            seen.remove(s[seen_counter])
            seen_counter += 1

        seen.add(ch)
        max_len = max(max_len, len(seen))

    return max_len