# Positional arguments
def power(a,b):
    return a**b

power_of_nums = power(2, 3)
# print(f"power_of_nums= {power_of_nums}")

# Keyword arguments
# def describe_person(name,age,designation):
#     print(f"{name} is a {age} years old and he is a {designation}")

# describe_person(age=38,designation='Software Engineer',name='Anil')

def describe_person(name,age,designation):
    print(f"{name} is a {age} years old and he is a {designation}")

# describe_person('Anil',38,designation='Software Engineer')

# default arguments
def increment(number, by=1):
    return number+by

incremented_value  = increment(5, 3)
print(f"incremented_value= {incremented_value}")

# Variable length Positional arguments (*args)


# Variable length Keyword arguments (**kwargs)
