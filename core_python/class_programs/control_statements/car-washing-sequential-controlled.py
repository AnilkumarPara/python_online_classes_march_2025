# WAP for the car washing and user can choose the person
# Sequential Statements

#person = input("Enter the person name: ")
#print(person, "will clean the car")
#print("Car cleaning started")
#print("Car cleaning is in progress")
#print("Car cleaning completed")

# Control statements
no_of_cars = int(input("Howmany number of cars available for the cleaning: "))
i=1
while i <= no_of_cars:
    car_cleaned_state = input(f"Is your car-{i} is in cleaned state enter Yes Otherwise Enter No: ")
    if car_cleaned_state == 'No':
        person = input("Enter the person name: ")
        print(person, "will clean the car")
        print(f"Car-{i} cleaning started")
        print(f"Car-{i} cleaning is in progress")
        print(f"Car-{i} cleaning completed")
    else:
        print(f"Your car-{i} is already in cleaned state. We no need to clean today")
    i = i+1


