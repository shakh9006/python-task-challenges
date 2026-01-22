# Source: https://www.codewars.com/kata/57faa6ff9610ce181b000028/train/python

# Title: Clean up after your dog

def crap(garden: list[list[str]], bags: int, cap: int) -> str:
    caps = bags * cap
    count_of_cp = 0

    for row in garden:
        if row.count('D'): return 'Dog!!'
        count_of_cp += row.count('@')

    return 'Clean' if caps >= count_of_cp else 'Cr@p'
