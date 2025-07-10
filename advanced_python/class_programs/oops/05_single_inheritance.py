class Employee:
    raise_amount = 0.1
    company_name = 'NDS'

    def __init__(self, name, dept_name, salary):
        self.name = name
        self.dept_name = dept_name
        self.salary = salary

    def display(self):
        print(self.name)
        print(self.dept_name)
        print(self.salary)

    def increase_salary(self):
        print(self.salary+(self.salary*self.raise_amount))

    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount


class Developer(Employee):
    raise_amount=0.15

    def __init__(self, name, dept_name,salary,prog_lang):
        super().__init__(name, dept_name, salary)
        self.prog_lang = prog_lang


dev1 = Developer('Anil', 'SARD', 20000,'Python')
dev2 = Developer('Sachin', 'IT', 10000, 'Java')
