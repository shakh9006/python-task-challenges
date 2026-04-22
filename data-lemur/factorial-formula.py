# Source: https://datalemur.com/questions/python-factorial-formula

# Title: Factorial Formula


def factorial(n):
    if n == 0:
        return 1

    return n * factorial(n - 1)


