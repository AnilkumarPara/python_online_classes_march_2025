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

class Manager(Employee):
    def __init__(self,name,dept_name,salary,employees=None):
        if employees is None:
            self.employees = []
        else:
            self.employees = employees
    def add_employee(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_employee(self,emp):
        if emp in self.employees:
            self.employees.remove(emp)


class DevManager(Developer, Manager):
    pass


dev1 = Developer('Sunil','SARD',10000, 'Python')
devmgr = DevManager('Anil','SARD',20000, 'Python')

print(devmgr.raise_amount)
devmgr.add_employee(dev1)
print(devmgr.company_name)
