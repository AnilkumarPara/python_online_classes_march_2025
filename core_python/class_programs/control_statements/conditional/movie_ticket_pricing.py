"""
Movie Ticket Pricing
Imagine a movie theater that offers different ticket prices
based on the age of the customer and the time of the day.
The rules might be as follows:

Regular price: $10
Children under 12 and seniors over 65 get a 50% discount.
Matinée show (before 5 PM) offers a 25% discount to all.
"""
regular_price = 10
person_age = int(input("Enter the age of a person"))
show_timings = int(input("Enter the show timings as per the 24 Hours time format"))
if (0 <= person_age < 12) or (person_age > 65):
    discount = regular_price*0.5
    print(f"Your getting the 50% discount on the regular price because you are a children or senior citizen")
    discounted_price = regular_price - discount
    print(f"Please pay {discounted_price} to get the movie ticket")
elif 0 < show_timings <= 17:
    discount = regular_price * 0.25
    print(f"Your getting the 25% discount on the regular price for the shows before 5 PM")
    discounted_price = regular_price - discount
    print(f"Please pay {discounted_price} USD to get the movie ticket")
elif 17 < show_timings <= 23:
    print(f"You will get 25% discount only for the shows before 5 PM ")
    print(f"Please pay {regular_price} USD to get the movie ticket")
elif show_timings < 0 or show_timings>23:
    print("Invalid show timings, please enter the timings between 0 and 23")

print("End of the Program")
