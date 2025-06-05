class Property:
    def __init__(self, name, daily_price, property_type):
        self.name = name
        self.daily_price = daily_price
        self.property_type = property_type

    def __str__(self):
        return f"{self.name} ({self.property_type})"

    def get_price(self):
        return self.daily_price


class RentalManager:
    def __init__(self):
        self.rentals = {}  # Property -> days
        self.discounts = {}  # Dictionary: property_type -> discount_percent

    def add(self, property, days):
        self.rentals[property] = days

    def remove(self, property):
        if property in self.rentals:
            del self.rentals[property]

    def applyDiscount(self, discount, prop_type):
        self.discounts[prop_type] = discount


    def __iter__(self):
        # Return an iterator over the keys (i.e., Property objects)
        return iter(self.rentals)

    def printSummary(self):
        total = 0
        for property, days in self.rentals.items():
            base_price = property.get_price()
            discount = self.discounts.get(property.property_type, 0)
            discounted_price = base_price * (1 - discount / 100)
            cost = discounted_price * days
            print(f"{property.name} for {days} days @{discounted_price:.1f}/day = {cost:.1f}")
            total += cost
        print(f"TOTAL = {round(total, 2)}")


# Example usage
p1 = Property("Seaside Villa", 150, "Villa")
p2 = Property("Urban Apartment", 90, "Apartment")

manager = RentalManager()
manager.add(p1, 3)
manager.add(p2, 2)

# Using the iterator
for property in manager:
    print(property)