# Nested function
# Defining a function inside a another function


def outer_func(msg):
    print("Outer function")
    print(f"outer_func= {msg}")
    def inner_func():
        print("Inner Function")
        print(f"outer_func= {msg}")
    return inner_func


inner = outer_func('Hello')
inner()
