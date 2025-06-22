# Variable length Positional arguments (*args)
def add(a, b):
    return a+b

sum_of_the_values = add(2, 3)
print(f"sum_of_the_values= {sum_of_the_values}")

def add(a,b,c):
    return a+b+c

sum_of_the_values_2 = add(2, 3, 4)
print(f"sum_of_the_values_2= {sum_of_the_values_2}")

def add(a,b,c, d):
    return a+b+c+d

sum_of_the_values_3 = add(2, 3, 4, 5)
print(f"sum_of_the_values_3= {sum_of_the_values_3}")

# Variable length Keyword arguments (**kwargs)
