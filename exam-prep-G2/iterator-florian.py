class RentalManager():
    def __init__(self):
        self.properties = []
        self.n = -1

    def __next__(self):
        self.n += 1
        if self.n >= len(self.properties):
            raise StopIteration
        return self.properties[self.n][0]

    def __iter__(self):
        self.n = -1
        return self

    def add(self, property, duration):
        self.properties.append((property, duration))

    def remove(self, property):
        for property_compare in self.properties:
            if property_compare[0] == property:
                self.properties.remove(property_compare)

    def applyDiscount(self, percentage, type):
        for property in self.properties:
            if property[0].type == type:
                property[0].price *= 1-(percentage/100)


class Property():
    def __init__(self, name, daily_rental_price, type):
        self.name = name
        self.price = daily_rental_price
        self.type = type

    def __str__(self):
        return f"{self.name} ({self.type})"

p1 = Property("Seaside Villa", 150, "Villa")
p2 = Property("Urban Apartment", 90, "Apartment")

manager = RentalManager()
manager.add(p1, 3)
manager.add(p2, 2)

manager.applyDiscount(20, "Villa")


for property in manager:
    print(property)

for property in manager:
    print(property)