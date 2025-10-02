# Source: https://leetcode.com/problems/search-insert-position/description/

# Title: Search Insert Position

# Description

"""
Given a sorted array of distinct integers and a target value,
return the index if the target is found.
If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.
"""


def search_insert(nums, target: int) -> int:
    count = len(nums)

    for i in range(count):
        if nums[i] == target:
            return i

        if nums[i] < target < nums[i + 1] and count > i + 1:
            return i + 1

        if nums[i] > target and i == 0:
            return i

    return count