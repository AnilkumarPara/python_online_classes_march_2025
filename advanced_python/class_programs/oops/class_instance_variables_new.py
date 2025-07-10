class Employee:
    company_name = 'Sony'
    raise_amount = 0.2
    total_no_of_employees = 0

    def __init__(self, name, dept_name, salary):
        self.name = name
        self.dept_name = dept_name
        self.salary = salary
        Employee.total_no_of_employees += 1


    def increase_salary(self):
        increment_amount = self.salary * self.raise_amount
        self.salary = self.salary + increment_amount


emp1 = Employee('Anil', 'SARD', 20000)
emp2 = Employee('Sachin', 'IT', 10000)
emp3 = Employee('Joshi', 'SARD', 5000)

print(Employee.total_no_of_employees)
print(emp1.total_no_of_employees)
print(emp2.total_no_of_employees)
print(emp3.total_no_of_employees)

# emp3.raise_amount=0.3
# emp1.increase_salary()
# emp2.increase_salary()
# emp3.increase_salary()
#
# print("emp1 sal", emp1.salary)
# print("emp2 sal", emp2.salary)
# print("emp3 sal", emp3.salary)