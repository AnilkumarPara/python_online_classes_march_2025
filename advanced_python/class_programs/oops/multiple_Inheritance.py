class Developer:
    raise_amount=0.15

    def __init__(self, name, dept_name, salary, prog_lang):
        self.name = name
        self.dept_name = dept_name
        self.salary = salary
        self.prog_lang = prog_lang

    def display(self):
        print(self.name)
        print(self.dept_name)
        print(self.salary)
        print(self.prog_lang)

    def increase_salary(self):
        print(self.salary+(self.salary*self.raise_amount))

    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

class TeamLead:
    raise_amount = 0.17

    def __init__(self, name, dept_name, salary, team_size):
        self.name =name
        self.dept_name = dept_name
        self.salary = salary
        self.team_size = team_size

    def display(self):
        print(self.name)
        print(self.dept_name)
        print(self.salary)
        print(self.team_size)

    def leading_team(self):
        print("He will lead the team")

class DevLead(Developer, TeamLead):
    raise_amount = 0.18
    def __init__(self,name, dept_name, salary, prog_lang,team_size):
        super().__init__(name, dept_name, salary, prog_lang)
        self.team_size = team_size

    def display(self):
        print(self.name)
        print(self.dept_name)
        print(self.salary)
        print(self.prog_lang)
        print(self.team_size)

dl = DevLead('Anil','SARD',25,'Python',5)
# print(dl.__dict__)

#__dict__
# this stores object attributes information in the form of dictionary

# For instance
# Instance attributes in the form of dictionary
# For classes
# It is going to return the attributes and methods

# dl.__dict__['name'] ='Sunil'
# print("After update")
# print(dl.__dict__)
print(Developer.__dict__)
