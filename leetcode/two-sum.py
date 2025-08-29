# Source: https://leetcode.com/problems/two-sum/description/

# Title: Two Sum

# Description

"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.
"""


def two_sum(nums, target):
    store = {}

    for i in range(len(nums)):
        current = nums[i]
        if current in store:
            return [store[current], i]

        left_val = target - current
        store[left_val] = i
    return [0, 0]