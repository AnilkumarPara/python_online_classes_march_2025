print("start")
def decorator(func):
    def wrapper_function(name, institute_name):
        print(f"\nHi {name},\n")
        func(name, institute_name)
        print("If you are Interested please contact us")
        print(f"\nRegards, \n{institute_name} Institute")
    return wrapper_function

@decorator
def start_courses(name, institute_name):
    print("We are starting with the following courses")
    print("Python, Java, C#")

start_courses('Sachin', 'Cranes')
# start_courses('Joshi', 'QSpiders')

# start_courses('Anil', 'JSpiders')

@decorator
def start_course(name, institute_name):
    print("We are starting with Python course")


start_course('John', 'Naresh Technologies')
# start_course('Thomas', 'QSpiders')