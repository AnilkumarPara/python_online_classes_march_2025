print("Start")


def decorator_function(func):
    def wrapper_function(name, institute_name):
        print(f"Hi {name}")
        func()
        print(f"Regards,{institute_name}")

    return wrapper_function


@decorator_function
def start_courses():
    print("We are staring with the following courses:")
    print("Python, Java, Selenium, Testing")


start_courses('Sachin', 'Naresh Technologies')


@decorator_function
def start_course():
    print("This is to inform you that we are going to start with the 'Python' Course")


start_course('John', 'Cranes')
