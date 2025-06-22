# def config(**settings):
#     for key, value in settings.items():
#         print(f"{key}: {value}")
#
#
# config(database="MySQL", port=3306, host="localhost")
# config(database="MySQL", port=3306, host="localhost", username='admin', password='admin')


def log_message(level, *args, **kwargs):
    print(f"Level: {level}")
    for arg in args:
        print(f"Message: {arg}")
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# Example usage
log_message("INFO", "This is a log message", "Another message", user="Alice", action="login")
