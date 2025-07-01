def decorator(func):
    def wrapper():
        print("Before calling the original function")
        func()
        print("After calling the original function")
    return wrapper
@decorator
def greet():
    print("Hello World!")
greet()

@decorator
def greeting():
    print("Hello Guys")

greeting()
