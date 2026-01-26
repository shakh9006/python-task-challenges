# Source: https://www.codewars.com/kata/587c37897f7dc251a0000001/train/python

# Title: Write your own map function.

def map(function, iterable):
    return [function(i) for i in iterable]