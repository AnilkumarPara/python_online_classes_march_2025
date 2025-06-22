def square_root(n):
    return n ** 0.5


square_func = square_root
print(f"square_root func= {square_root}")
print(f"square_func = {square_func}")
print(square_root(5))

print(square_func(5))