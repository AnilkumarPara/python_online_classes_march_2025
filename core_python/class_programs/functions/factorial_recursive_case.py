def factorial(number):
    if number>=0:
        # Base Case
        if number == 1 or number==0:
            return 1
        else:
            # recursive case
            return number * factorial(number-1)

    else:
        return "factorial can't be found for the negative numbers"

n = int(input("Enter a number to find the factorial"))
fact = factorial(n)
print(f"factorial of {n} is {fact}")
