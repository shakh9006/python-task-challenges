# Source: https://leetcode.com/problems/longest-common-prefix/description/

# Title: Longest Common Prefix

# Description

"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".
"""


def longest_common_prefix(words) -> str:
    pref = words[0]
    pref_len = len(pref)

    for s in words[1:]:
        while pref != s[0:pref_len]:
            pref_len -= 1
            if pref_len == 0:
                return ""

            pref = pref[0:pref_len]

    return pref