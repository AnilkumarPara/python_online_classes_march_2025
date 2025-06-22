"""
Creating a dictionary of squares for numbers from 1 to 5
using dictionary comprehension
"""
numbers = [1, 2, 3, 4, 5]
sq_dict = {}
for n in numbers:
    sq_dict.setdefault(n, n*n)
print(sq_dict)
