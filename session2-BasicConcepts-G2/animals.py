
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.is_alive = True
        self.is_dead = False

    def describe(self):
        print(f"I am an Animal, my name is {self.name}, I am {self.age} years old")

    @classmethod
    def sound(cls):
        print("Baaaah!")

fishcount = 0

class Fish(Animal):

    def __init__(self, name, age, speed):
        name = "Fish " + name
        super().__init__(name, age)
        # self.name = name
        # self.age = age
        self.speed = speed

    def clean_bowl(self):
        print(f"{self.name}'s bowl is now clean. Thanks.")

    def describe(self):
        print(f"I am a very cool Fish! My name is {self.name}.")
        # super().describe()

    def __str__(self):
        return f"I am a very cool Fish! My name is {self.name}."

    @classmethod
    def sound(cls):
        print("Blubb!")

class FWF(Fish):
    pass

class Carp(FWF):
    pass

# print(int.__mro__)
# print("\n\n\n")

class Dog(Animal):
    def describe(self):
        print(f"Dogs are anonymous spies. Don't ask.")

# a = Animal("Bob", 23)
# a.describe()
#
# f = Fish("Stefan", 3)
# f.describe()
# f.clean_bowl()

# d = Dog("Lisa", 3)
# d.describe()
# d.clean_bowl()

pets = [
    Animal("Bob", 23),
    Fish("Stefan", 3),
    Dog("Alice", 12),
    Fish("Lisa", 7)
]

Fish("Stefan", 3).sound()

print(Fish.fishcount)

# for pet in pets:
#     pet.describe()

# for pet in pets:
#     if isinstance(pet, (Fish, Dog)):
#         print(pet.name, pet.age, "is a fish or a Dog")
#     else:
#         print(pet.name, pet.age, "is a generic animal")


# print(pets[1].__class__)

# print(issubclass(Fish, Animal))

# print(str(pets[-1]))

def animalAge(animal: Animal) -> None:  # This function expects an object of type Anmial
    someVar: str = "hello"
    print("animal's age is ", animal.age)

animalAge("haha, this does not work.")