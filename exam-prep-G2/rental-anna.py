class RentalManager:
    def __init__(self):
        self.properties = []

    def add(self, prop, days):
        self.properties.append((prop, days))
        print("added")

    def remove(self, prop):
        for p in self.properties:
            if p[0] == prop:
                self.properties.remove(p)
        print("removed.")

    def apply_discount(self, percentage, type):
        for prop, days in self.properties:
            if prop.type == type:
                prop.daily_rental_price = prop.daily_rental_price * (1 - percentage / 100)

    def print_summary(self):
        total = 0
        for prop, days in self.properties:
            total += prop.daily_rental_price * days
            print(f"{prop.name} for {days} days @{prop.daily_rental_price}/day = {prop.daily_rental_price * days}")
        print(f"TOTAL = {total}")


class Property(object):
    def __init__(self, name, daily_rental_price, type):
        self.name = name
        self.daily_rental_price = daily_rental_price
        self.type = type


# what we want to have:
p1 = Property("Seaside Villa", 150, "Villa")
p2 = Property("Urban Apartment", 90, "Apartment")
# p3 = Property("Sun-Side Villa", 150, "Villa")

manager = RentalManager()
manager.add(p1, 3)
manager.add(p2, 2)
# manager.add(p3, 4)
# manager.remove(p1)

manager.apply_discount(20, "Villa")
manager.print_summary()

"""
Seaside Villa for 3 days @120.0/day = 360.0
Urban Apartment for 2 days @90.0/per day = 180.0
TOTAL = 540.0
"""
