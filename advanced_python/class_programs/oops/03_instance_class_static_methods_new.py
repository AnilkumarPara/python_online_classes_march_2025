import datetime
class Employee:
    company_name = 'NDS'
    total_no_of_employees = 0


    def __init__(self, name, dept_name, salary):
        self.name = name
        self.dept_name = dept_name
        self.salary = salary
        Employee.total_no_of_employees += 1

    def display(self):
        print(self.name)
        print(self.dept_name)
        print(self.salary)


    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def set_company_name(cls, company_name):
        cls.company_name = company_name

    @staticmethod
    def is_working_day(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        else:
            return True

emp1 = Employee('Anil', 'SARD', 20000)
emp2 = Employee('Sachin', 'IT', 10000)
emp3 = Employee('Joshi', 'SARD', 5000)
#
emp1.display()
# emp2.display()
# emp3.display()
Employee.set_raise_amount(0.1)
print(Employee.raise_amount)
Employee.set_company_name('Cisco')
print(Employee.company_name)
day = datetime.date(2025,6,3)
print(f"day = {day}")
print(emp1.is_working_day(day))

