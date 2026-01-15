# Source: https://www.codewars.com/kata/580a4734d6df748060000045/train/python

# Title: Sorted? yes? no? how?

def is_sorted_and_how(arr):
    asc_arr = sorted(arr)
    if asc_arr == arr:
        return "yes, ascending"

    desc_arr = sorted(arr, reverse=True)
    if desc_arr == arr:
        return "yes, descending"

    return "no"