import math

# input : [1, 2, 3, 4]
# output: [1.0, 1.414, 1.732, 2.0]

def square_root(n):
    return n ** 0.5


def square(n):
    return n ** 2


def cube(n):
    return n ** 3


def log10_calculator(number):
    return math.log10(number)

# Function as an argument to a function
def my_list_map(func, numbers):
    result = []
    for num in numbers:
        result.append(func(num))
    return result


print(my_list_map(square_root, [1, 2, 3, 4]))
print(my_list_map(square, [1, 2, 3, 4]))
print(my_list_map(cube, [1, 2, 3, 4]))
print(my_list_map(log10_calculator, [1, 2, 3, 4]))
