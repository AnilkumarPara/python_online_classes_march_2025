def greeting_time_of_day(time_of_day):
    def morning_greet(name):
        return f"Good morning, {name}!"

    def afternoon_greet(name):
        return f"Good afternoon, {name}!"

    def evening_greet(name):
        return f"Good evening, {name}!"

    if time_of_day == "morning":
        return morning_greet
    elif time_of_day == "afternoon":
        return afternoon_greet
    else:
        return evening_greet


# Create a greeting function for the morning
morning_greeting = greeting_time_of_day("morning")
print(morning_greeting("Alice"))  # Output: Good morning, Alice!

# Create a greeting function for the afternoon
afternoon_greeting = greeting_time_of_day("afternoon")
print(afternoon_greeting("Bob"))  # Output: Good afternoon, Bob!

# Create a greeting function for the evening
evening_greeting = greeting_time_of_day("evening")
print(evening_greeting("Charlie"))  # Output: Good evening, Charlie!
