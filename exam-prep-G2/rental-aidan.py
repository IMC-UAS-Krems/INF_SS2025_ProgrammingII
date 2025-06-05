from typing import List
# RM: Add and remove properties
# Prop Class: name, daily price, and type
# applyDiscount applies discount to all properties of a certain type

class RentalManager(object):
    def __init__(self) -> None:
        self.prop_list: List[tuple] = []

    def add(self, prop: "Property", days: int) -> None:
        self.prop_list.append((prop, days))

    def apply_discount(self, percent: float, prop_type: str) -> None:
        for i in self.prop_list:
            if i[0].type == prop_type:
                i[0].daily_rent_price *= (1 - (percent / 100))


    def print_summary(self) -> None:
        total: float = 0
        for i in self.prop_list:
            print(f"{i[0].name} for {i[1]} days @{i[0].daily_rent_price}/day = {i[0].daily_rent_price * i[1]}")
            total += i[0].daily_rent_price * i[1]

        print(f"TOTAL = {total}")


class Property(object):
    def __init__(self, name: str, daily_rent_price: float, type: str) -> None:
        self.name = name
        self.daily_rent_price = float(daily_rent_price)
        self.type = type


p1 = Property("Seaside Villa", 150, "Villa")
p2 = Property("Urban Apartment", 90, "Apartment")

manager = RentalManager()
manager.add(p1, 3)
manager.add(p2, 2)

manager.apply_discount(20, "Villa")
manager.print_summary()