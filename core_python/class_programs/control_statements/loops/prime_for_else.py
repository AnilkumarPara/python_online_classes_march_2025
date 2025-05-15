# Find the Given number is prime or not
n = int(input("Enter a integer number"))

if n==0 or n==1:
    print(f"{n} is not a Prime Number")
elif n>=2:
    counter = 0
    for i in range(1, n+1):
        if n%i == 0:
            counter = counter + 1
        if counter == 3:
            print(f"{n} is not a Prime Number")
            break
    else:
        print(f"{n} is a Prime Number")

else:
    print(f"We can't find the Prime number for the negative number {n}")
