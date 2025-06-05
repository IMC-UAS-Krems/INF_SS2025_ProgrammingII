class RentalManager:
    def __init__(self):
        self.properties = []
        self.__props_only = []
        self.types = {}

    def add(self, prop, nights):
        self.properties.append((prop, nights))
        self.__props_only.append(prop)


    def remove(self, prop):
        self.properties.remove(prop)

    def applyDiscount(self, percent, type):
        self.types[type] = percent

    def printSummary(self):
        total = 0
        for prop, nights in self.properties:
            for type, discount in self.types.items():
                if prop.type == type:
                    total += (prop.daily_rental_price * nights) - (prop.daily_rental_price * nights * discount/100)
                    print(f"{prop.name} for {nights} days @{prop.daily_rental_price:.1f}/day = {prop.daily_rental_price * nights}")
                else:
                    total += prop.daily_rental_price * nights
                    print(f"{prop.name} for {nights} days @{prop.daily_rental_price:.1f}/day = {prop.daily_rental_price * nights}")

        print(f"TOTAL = {total}\n")


    def __iter__(self):
        return ManagerIterator(self.__props_only)



class Property:
    def __init__(self, name, daily_rental_price, type):
        self.name = name
        self.daily_rental_price = daily_rental_price
        self.type = type


p1 = Property("Seaside Villa", 150, "Villa")
p2 = Property("Urban Apartment", 90, "Apartment")

manager = RentalManager()
manager.add(p1, 3)
manager.add(p2, 2)
manager.applyDiscount(20, "Villa")
manager.printSummary()


class ManagerIterator:
    def __init__(self, properties):
        self.properties = properties
        self.start = -1

    def __next__(self):
        self.start += 1
        if self.start >= len(self.properties):
            raise StopIteration
        else:
            return f"{self.properties[self.start].name} ({self.properties[self.start].type})"

for prop in manager:
    print(prop)