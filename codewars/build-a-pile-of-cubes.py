# Source: https://www.codewars.com/kata/5592e3bd57b64d00f3000047/train/python

# Title: Build a pile of Cubes

def find_nb(m):
    n = 1
    volume = 0

    while volume < m:
        volume += n ** 3
        if volume == m:
            return n
        n += 1

    return -1