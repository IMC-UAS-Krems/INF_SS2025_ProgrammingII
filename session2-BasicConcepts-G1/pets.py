class Pet:
    def __init__(self, name):
        self.name = name

    def feed(self):
        print(f"I am a Pet {self.name}. I eat food.")

    def __str__(self):
        return f"A generic Pet named {self.name}"

class Fish(Pet):

    def feed(self):
        print(f"I am Fish {self.name}. I eat special fish food.")

    def clean_fishbowl(self):
        print(f"Hi, I am {self.name}. Thanks for cleaning my bowl.")

    def __str__(self):  # overrides Pet.__str__(self):
        return f"Fish are awesome. I love them so much. This one is called {self.name}"

class FreshWaterFish(Fish):
    pass

class Carp(FreshWaterFish):
    pass

class Salmon(FreshWaterFish):
    pass


pets = [
    Pet("Dog1"),
    Carp("Frank"),
    Pet("Dog2"),
    Salmon("Mary"),
]

for pet in pets:
    pet.feed()

for pet in pets:
    if isinstance(pet, Fish):
        pet.clean_fishbowl()

for pet in pets:
    # print(f"A generic Pet named {pet.name}")
    print(str(pet))

for pet in pets:
    if isinstance(pet, Fish):
        print(f"Fish are awesome. this one is {pet.name}")
    else:
        print(f"This is another boring pet {pet.name}")



def len(obj):
    if "__len__" in obj.__dict__:
        return obj.__len__()
    else:
        raise