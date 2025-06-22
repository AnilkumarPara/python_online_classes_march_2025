import pytest


def main():
    print("my_own_function")
    print("I am in the first program and this should be executed whenever I run the script directly")
    return True

def common_function():
    print("This is a common function and shouldn't be executed at any point of time")
    return False


if __name__ == '__main__':
    main()
    common_function()



