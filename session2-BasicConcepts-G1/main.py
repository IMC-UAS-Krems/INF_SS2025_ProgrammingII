
class Pet():
    name = ""
    age = 0
    owner = ""
    sound = ""

    def speak(self):
        print(f"{self.name} says: '{self.sound}!'")

class Thing():
    owner = ""
    age = ""

fluffy = Pet()
fluffy.name = "Fluffy"
fluffy.age = 3
fluffy.owner = "Stefan"
fluffy.sound = "Meow!"

fluffy.speak()


def speak(self):
    print(f"{self.name} says: '{self.sound}!'")

speak(fluffy)

bottle = Thing()
bottle.owner = "Stefan"
bottle.age = 1

speak(bottle)