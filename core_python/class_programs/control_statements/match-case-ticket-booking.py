# WAP to book the movie ticket based on the user choice
class_type = input("Enter the Class Name to book the movie ticket: ")
match class_type:
    case 'Diamond':
        print("We are booking the ticket for the Diamond class")
        print("Please pay the money")
        print("Your ticket is booked successfully for the Diamond class")
    case 'Gold':
        print("We are booking the ticket for the Gold class")
        print("Please pay the money")
        print("Your ticket is booked successfully for the Gold class")
    case 'Silver':
        print("We are booking the ticket for the Silver class")
        print("Please pay the money")
        print("Your ticket is booked successfully for the Silver class")
    case _:
        print("You have entered the invalid class, please enter the Diamond or Gold or Silver ")
print("End of the program")
