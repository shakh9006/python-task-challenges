# Source: https://leetcode.com/problems/median-of-two-sorted-arrays/description/

# Title: Median of Two Sorted Arrays

# Description

"""
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
The overall run time complexity should be O(log (m+n)).
"""

import math

def find_median_sorted_arrays(nums1, nums2):
    merged = sorted(nums1 + nums2)
    idx = math.floor(len(merged) / 2)
    if len(merged) % 2 == 0:
        return (merged[idx] + merged[idx - 1]) / 2
    else:
        return merged[round(idx)]