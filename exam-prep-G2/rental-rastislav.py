class RentalManager():
    def __init__(self, ):
        self.properties = {}

    def add(self, property, days):
        self.properties[property] = days

    def applyDiscount(self, discount, rentaltype):
        for property in self.properties:
            if property.type == rentaltype:
                property.price = property.price * (100 - discount) / 100

    def printSummary(self):
        total = 0
        for property, days in self.properties.items():
            totalforprop = property.price * days
            total += totalforprop
            print(f"{property.name} for {days} days @ {property.price}/day = {totalforprop}")
        print("TOTAL =", total)


class Property():
    def __init__(self, name, dailyrentalprice, type):
        self.name = name
        self.price = dailyrentalprice
        self.type = type
        self.days = 0


p1 = Property("Seaside Villa", 150, "Villa")
p2 = Property("Urban Appartment", 90, "Apartment")

manager = RentalManager()
manager.add(p1, 3)
manager.add(p2, 2)
manager.applyDiscount(20, "Villa")
manager.printSummary()

