correct_password = 'Python123'
start_attempt = 1
while start_attempt<=5:
    password = input("Enter the password for the authentication: ")
    if correct_password == password:
        print("User has entered the correct Password")
        print("Password Authentication is successful")
        break
    else:
        print("User has entered the incorrect Password, Try Again")
    start_attempt = start_attempt+1
else:
    print("You have reached the maximum number of attempts")

print("End of the program")
