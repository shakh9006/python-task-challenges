from timeit import default_timer as timer
import math
import time

def measure_time(func):
    def wrapper(*args, **kwargs):
        start = timer()

        func(*args, **kwargs)

        end = timer()

        print(f"Function {func.__name__} took {end - start} for execution")

    return wrapper

@measure_time
def factorial(num):
    time.sleep(3)
    print(math.factorial(num))

factorial(5)