class Property:
    def __init__(self, name: str, price: float, kind: str):
        self.name = name
        self.price = price
        self.kind = kind


class RentalManager:
    def __init__(self):
        self.property_list: list[Property] = []
        self.property_discounts: dict[Property:float] = {}
        self.remaining_property_days: dict[Property:int] = {}

    def add_property(self, property: Property, days: int) -> None:
        self.property_list.append(property)
        self.property_discounts[property.kind] = 0
        self.remaining_property_days[property] = days

    def remove_property(self, property: Property) -> None:
        self.property_list.remove(property)
        del self.property_discounts[property.kind]

    def apply_discount(self, kind: str, discount: float) -> None:
        if not kind in self.property_discounts:
            return

        self.property_discounts[kind] = discount

    def next_day(self) -> None:
        for property, days in self.remaining_property_days.items():
            if days < 1:
                del self.remaining_property_days[property]
                return

            self.remaining_property_days[property] -= 1

    def print_summary(self) -> None:
        total_price = 0.0
        for property in self.property_list:
            days = self.remaining_property_days[property]
            actual_price = property.price * (1 - self.property_discounts[property.kind] / 100.0)
            whole_price = actual_price * days
            total_price += whole_price
            print(f"{property.name} for {days} @{actual_price}/day = {whole_price}")

        print("TOTAL =", total_price)


p1 = Property("Seaside Villa", 150, "Villa")
p2 = Property("Urban Apartment", 90, "Apartment")

manager = RentalManager()
manager.add_property(p1, 3)
manager.add_property(p2, 2)

manager.apply_discount("Villa", 20)

manager.print_summary()

manager.next_day()

manager.print_summary()