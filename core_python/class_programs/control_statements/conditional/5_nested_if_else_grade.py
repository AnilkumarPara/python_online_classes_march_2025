"""
Find the class in which student has passed in the exam
based on the percentage of marks
"""
percentage = float(input("Enter the percentage of marks secured in the final exams"))
if 70 <= percentage <= 100:
    print("Student has passed in the Distinction")
else:
    if 60 <= percentage < 70:
        print("Student has passed in the First Class")
    else:
        if 50 <= percentage < 60:
            print("Student has passed in the Second Class")
        else:
            if 35 <= percentage < 50:
                print("Student has passed in the Third Class")
            else:
                if 0 <= percentage < 35:
                    print("Student has failed in the exams successfully")
                else:
                    print("Student has entered the invalid marks, please enter the marks in the range of 0 to 100")
print("End of the program")
