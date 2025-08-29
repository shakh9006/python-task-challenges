# Source: https://www.codewars.com/kata/556196a6091a7e7f58000018/train/python

# Title: Largest pair sum in array

# Description

# Given a sequence of numbers, find the largest pair sum in the sequence.

def largest_pair_sum(numbers):
    s = sorted(numbers)
    return s[-1] + s[-2]
