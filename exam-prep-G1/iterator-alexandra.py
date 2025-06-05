class Property():
    def __init__(self, name: str, price: float, type: str, discount=0.00):
        self.name = name
        self.price = price
        self.type = type
class RentalManager():
    def __init__(self):
        self.properties = {}
        self.discounts = {}

    def __iter__(self):
        return PropertyIterator(self.properties)

    def add(self, property: Property, duration: int):
        self.properties.update({property: duration})


    def remove(self, property: Property):
        if property in self.properties:
            del self.properties[property]

    def applyDiscount(self, discount, type):
        for property, duration in self.properties.items():
            if property.type == type:
                property.price = property.price - property.price * (discount / 100)


    def printSummary(self):
        total_price = 0
        for property, duration in self.properties.items():
            total = property.price * duration
            print(f"{property.name} for {duration} days @{property.price}/day = {total}")
            total_price += total
            print(f"TOTAL = {total_price}")


class PropertyIterator():
    def __init__(self, properties):
        self.properties = list(properties.items())
        self.count = -1

    def __next__(self):
        self.count += 1
        if len(self.properties) <= self.count:
            raise StopIteration
        return f"{self.properties[self.count][0].name} ({self.properties[self.count][0].type})"

p1 = Property("Seaside Villa", 150, "Villa")
p2 = Property("Urban Apartment", 90, "Apartment")
manager = RentalManager()
manager.add(p1, 3)
manager.add(p2, 2)
# manager.printSummary()
# print("\nDiscount test:")
manager.applyDiscount(20, "Villa")
# manager.printSummary()
print("\nProperty iterator:")
for property in manager:
    print(property)
