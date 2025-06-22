def add(*args):
    sum_of_the_values = 0
    for arg in args:
        sum_of_the_values = sum_of_the_values + arg
    return sum_of_the_values



sum_of_the_values_1 = add(2, 3, 4)
print(f"sum_of_the_values_1= {sum_of_the_values_1}")

sum_of_the_values_2 = add(2, 3)
print(f"sum_of_the_values_2= {sum_of_the_values_2}")

sum_of_the_values_3 = add(2, 3, 4,5,6)
print(f"sum_of_the_values_3= {sum_of_the_values_3}")
