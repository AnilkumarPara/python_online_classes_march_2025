# In Python we have 4 function types


# 1. Function without arguments and without return value
def greeting_message():
    print("Hello")

# greeting_message()

# 2. Function with arguments and no return value
def greeting_message(name):
    print(f"Hello {name}")

# greeting_message('Anil')

# 3. Function with arguments and with return value

def add(a,b):
    return a+b

# addition = add(2, 3)
# print(f"sum of the values= {addition}")


# 4. Function without arguments and with return value
def retrieve_pi_value():
    return 3.14

pi = retrieve_pi_value()
print(f"PI value= {pi}")
