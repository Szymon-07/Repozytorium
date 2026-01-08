# Klasa bazowa - Nieruchomość
class Property:
    def __init__(self, area: float, rooms: int, price: float, address: str):
        self.area = area
        self.rooms = rooms
        self.price = price
        self.address = address

    def __str__(self):
        return f"Nieruchomość: {self.address} | {self.area}m2 | {self.price} PLN"


# Klasa dziedzicząca - Dom (ma dodatkowo pole plot - działka)
class House(Property):
    def __init__(self, area: float, rooms: int, price: float, address: str, plot: int):
        # super().__init__ wywołuje konstruktor z klasy wyżej (Property)
        super().__init__(area, rooms, price, address)
        self.plot = plot

    def __str__(self):
        return f"DOM: {self.address} | Powierzchnia: {self.area}m2 | Działka: {self.plot}m2 | Cena: {self.price}"


# Klasa dziedzicząca - Mieszkanie (ma dodatkowo pole floor - piętro)
class Flat(Property):
    def __init__(self, area: float, rooms: int, price: float, address: str, floor: int):
        super().__init__(area, rooms, price, address)
        self.floor = floor

    def __str__(self):
        return f"MIESZKANIE: {self.address} | Piętro: {self.floor} | {self.area}m2 | Cena: {self.price}"


# Testowanie
dom = House(area=150, rooms=5, price=850000, address="Dębowa 5", plot=1000)
mieszkanie = Flat(area=45, rooms=2, price=350000, address="Lipowa 10/4", floor=2)

print(dom)
print(mieszkanie)
