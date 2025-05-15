# WAP to print the squared number pattern
"""
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
"""
rows = int(input("Enter the No. of rows to be printed for square pattern"))
cols = int(input("Enter the No. of columns to be printed for square pattern"))
if rows == cols:
    print("We are going to design square pattern")
    for row in range(1, rows+1):
        for col in range(1, cols+1):
            print(1, end=' ')
        print()

else:
    print("We can't have the square pattern")
