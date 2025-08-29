# Source: https://www.codewars.com/kata/59c3e8c9f5d5e40cab000ca6/train/python

# Description

# Your task is to create a function called sum_arrays(),
# which takes two arrays consisting of integers, and returns the sum of those two arrays.

# The twist is that (for example) [3,2,9] does not equal 3 + 2 + 9, it would equal '3' + '2' + '9' converted to an integer for this kata,
# meaning it would equal 329. The output should be an array of the sum in a similar fashion to the input (for example, if the sum is 341,
# you would return [3,4,1]). Examples are given below of what two arrays

def sum_arrays(array1, array2):
    if not array1: return array2
    if not array2: return array1

    arr1 = ''.join(map(str, array1))
    arr2 = ''.join(map(str, array2))

    result = int(arr1) + int(arr2)
    output = [int(x) for x in str(result) if x != '-']

    if result < 0:
        output[0] = output[0] * -1

    return output