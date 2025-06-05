class Property:
    def __init__(self, name: str, price: float, kind: str):
        self.name = name
        self.price = price
        self.kind = kind

    def __str__(self) -> str:
        return f"{self.name} ({self.kind})"

class PropertyIterator:
    def __init__(self, property_list: list[Property]):
        self.property_list = property_list
        self.index = 0

    def __next__(self):
        if self.index >= len(self.property_list):
            raise StopIteration

        property = self.property_list[self.index]
        self.index += 1
        return property

class RentalManager:
    def __init__(self):
        self.property_list: list[Property] = []
        self.property_discounts: dict[Property:float] = {}
        self.remaining_property_days: dict[Property:int] = {}

    def __iter__(self) -> PropertyIterator:
        return PropertyIterator(self.property_list)

    def add_property(self, property: Property, days: int) -> None:
        self.property_list.append(property)
        if not property.kind in self.property_discounts:
            self.property_discounts[property.kind] = 0
        self.remaining_property_days[property] = days

    def remove_property(self, property: Property) -> None:
        kind = property.kind
        self.property_list.remove(property)
        del self.remaining_property_days[property]

        for property in self.property_list:
            if kind == property.kind:
                return

        del self.property_discounts[property.kind]

    def apply_discount(self, kind: str, discount: float) -> None:
        if not kind in self.property_discounts:
            return

        self.property_discounts[kind] = discount

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

for property in manager:
    print(property)