class Property:
    def __init__(self, name: str, price: float, base: str):
        self.name = name
        self.price = price
        self.base = base

class RentalManager:
    def __init__(self):
        self.cart = []

    def add(self, property: Property, days: int):
            self.cart.append((property, days))
    def remove(self, property: Property):
        for tup in self.cart:
            if tup[0] == property.name:
                self.cart.remove(tup)

    def applyDiscount(self, percentage: int, base: str):
        for tup in self.cart:
            if tup[0].base == base:
                tup[0].price = tup[0].price / 100 * (100 - percentage)

    def printSummary(self):
        total = 0
        for tup in self.cart:
            total += tup[0].price * tup[1]
        for tup in self.cart:
            print(f"{tup[0].name} for {tup[1]} days @{tup[0].price}/day = {tup[0].price * tup[1]}")
        print(f"TOTAL = {total}")

p1 = Property("Seaside Villa", 150, "Villa")
p2 = Property("Urban Apartment", 90, "Apartment")

manager = RentalManager()
manager.add(p1, 3)
manager.add(p2, 2)
manager.applyDiscount(20, 'Villa')
manager.printSummary()