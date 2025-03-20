
class Dog:
    def __init__(self, name, age, owner):
        self.name = name
        self.age = age
        self.owner = owner

    def describe(self):
        print(f"This is {self.name} it is {self.age} years old and owned by {self.owner}")

class Thing:
    def __init__(self, type, owner):
        self.type = type
        self.owner = owner

    def describe(self):
        print(f"This is a {self.type} and owned by {self.owner}")


lassie = Dog('Lassie', 3, 'Stefan')
lassie.describe()

bottle = Thing('Bottle', 'Stefan')
bottle.describe()