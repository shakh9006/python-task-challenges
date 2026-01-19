# Source: https://www.codewars.com/kata/525f3eda17c7cd9f9e000b39/train/python

# Title: Calculating with Functions

def zero(fn=None): return 0 if fn is None else fn(0)
def one(fn=None): return 1 if fn is None else fn(1)
def two(fn=None): return 2 if fn is None else fn(2)
def three(fn=None): return 3 if fn is None else fn(3)
def four(fn=None): return 4 if fn is None else fn(4)
def five(fn=None): return 5 if fn is None else fn(5)
def six(fn=None): return 6 if fn is None else fn(6)
def seven(fn=None): return 7 if fn is None else fn(7)
def eight(fn=None): return 8 if fn is None else fn(8)
def nine(fn=None): return 9 if fn is None else fn(9)

def plus(y): return lambda x: x + y
def minus(y): return lambda x: x - y
def times(y): return lambda x: x * y
def divided_by(y): return lambda x: x // y