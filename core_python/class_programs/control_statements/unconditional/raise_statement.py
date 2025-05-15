def my_function(x):
    if x<0:
        raise ValueError("X must be a non-negative")
    return x

my_function(-1)
