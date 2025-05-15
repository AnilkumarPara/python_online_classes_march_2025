# Find the maximum number in a list
numbers = [200,1, 2, 3, 4, 5, -1]
max_number = numbers[0]
for number in numbers:
    if max_number < number:
        max_number = number

print(f'max_number= {max_number}')
print("End of the Program")
