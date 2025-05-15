# Find the greatest of 3 numbers
a = int(input("Enter the number a: "))
b = int(input("Enter the number b: "))
c = int(input("Enter the number c: "))
if a>b:
    if a>c:
        print("a is greater")
    else:
        print("c is greater")
else:
    if b>c:
        print("b is greater")
    else:
        print("c is greater")
