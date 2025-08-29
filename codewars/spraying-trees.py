# Source: https://www.codewars.com/kata/5981a139f5471fd1b2000071/train/python

# Title: Spraying trees

# Description
"""
There are five workers : James, John, Robert, Michael and William. They work in a fixed order from Monday to Friday,
and they rest on weekends. The order of work is as follows:

James works on Monday,
John works on Tuesday,
Robert works on Wednesday,
Michael works on Thursday,
William works on Friday.

Your task is to create a function that takes three arguments:
Weekday: The day of the week (e.g., Monday).
Number of Trees: The number of trees that must be sprayed on that day.
Cost per Litre: The cost of 1 litre of liquid needed to spray a tree. Assume that 1 tree requires 1 litre of liquid.
The total cost of the liquid to spray all trees is denoted as x.
The function should return a string in the following format:
'It is (weekday) today, (name), you have to work, you must spray (number) trees and you need (x) dollars to buy liquid'
"""

def task(w, n, c):
    names = {
        'Monday': 'James',
        'Tuesday': 'John',
        'Wednesday': 'Robert',
        'Thursday': 'Michael',
        'Friday': 'William',
    }

    return f'It is {w} today, {names.get(w)}, you have to work, you must spray {n} trees and you need {n * c} dollars to buy liquid'
