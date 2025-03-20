
class Company(object):
    def __init__(self, name):
        self.name = name
        # self.employees = []


class Student(object):
    def __init__(self, name):
        self.name = name
        self.company = None

imc = Company("IMC")

max = Student("Max")
max.company = imc
john = Student("John")

print(f"Max's company is {max.company.name}")
print(f"John's company is {john.company}")
