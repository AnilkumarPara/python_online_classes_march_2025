n = 6

if n>=0:
# Initialize the factorial variable to 1
    fact = 1

    # Calculate the factorial using a for loop
    for i in range(1, n + 1):
        fact *= i

    print(fact)
else:
    print("factorial can't be found for the negative numbers")
