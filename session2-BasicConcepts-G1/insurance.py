

class Person:
    def __init__(self, ID, name, adress):
        self.ID = ID
        self.name = name
        self.adress = adress

    def identify_yourself(self):
        print(f"I am Person {self.name}")

    def abcd(self):
        print("abcd")

class Customer(Person):

    def __init__(self, ID, name, address, status):
        # super().__init__(ID, name, address)
        self.status = status

    def identify_yourself(self):
        # super().identify_yourself()
        print(f"I am also a Customer ({self.name})")

    def pay_fee(self):
        print("Thanks for paying")

    def abcd(self):  # This is the way we can imagine inheriting methods
        super().abcd()

class Agent:
    def __init__(self, ID, name, adress):
        self.ID = ID
        self.name = name
        self.adress = adress


# p = Person(2, "Tom", "IMC 3")
# p.identify_yourself()

c = Customer(1, "Stefan", "IMC 1")
# c.pay_fee()
c.identify_yourself()

# p.pay_fee()
