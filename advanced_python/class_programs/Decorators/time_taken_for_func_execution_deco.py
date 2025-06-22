"""
practical example where a decorator is used for timing the
execution of a function. This is a common use case in performance
analysis, where you want to measure how long a particular
piece of code takes to run without cluttering the code itself
with timing logic.
"""
import time


def time_it(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} took {end_time - start_time:.4f} seconds to execute")
        return result

    return wrapper


@time_it
def some_function(delay_time):
    """Function that simulates doing some work by sleeping for a given amount of time."""
    time.sleep(delay_time)
    print("Function execution completed.")


some_function(2)
