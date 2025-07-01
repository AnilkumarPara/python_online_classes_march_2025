def welcome_message():
    print("Welcome to the party")


def thankyou_message():
    print("Thanks for attending the party")

funcs = [welcome_message, thankyou_message]

for func in funcs:
    func()

