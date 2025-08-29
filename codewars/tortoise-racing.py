# Source: https://www.codewars.com/kata/55e2adece53b4cdcb900006c/train/python

# Title: Tortoise racing

# Description

"""
Two tortoises named A and B must run a race. A starts with an average speed of 720 feet per hour.
Young B knows she runs faster than A, and furthermore has not finished her cabbage.

When she starts, at last, she can see that A has a 70 feet lead but B's speed is 850 feet per hour.
How long will it take B to catch A?
"""

def race(v1, v2, g):
    t = 3600 * g / (v2-v1)
    return [t / 3600, t / 60 % 60, t % 60] if v2 > v1 else None
