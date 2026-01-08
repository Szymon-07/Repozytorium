import requests
from typing import List


# Definicja klasy Brewery (Browar)
class Brewery:
    # Konstruktor z typowaniem (inicjalizacja obiektu)
    def __init__(self, name: str, city: str, state: str, country: str):
        self.name = name
        self.city = city
        self.state = state
        self.country = country

    # Magiczna metoda __str__ - decyduje o tym, co się wyświetli, gdy zrobisz print(obiekt)
    def __str__(self) -> str:
        return f"Browar: {self.name} | Lokalizacja: {self.city}, {self.state} ({self.country})"


def pobierz_browary() -> None:
    # Adres API (pobieramy 20 sztuk)
    url = "https://api.openbrewerydb.org/v1/breweries?per_page=20"

    # Wykonanie połączenia (GET)
    response = requests.get(url)

    # Sprawdzenie czy połączenie się udało (kod 200 to OK)
    if response.status_code == 200:
        dane_json = response.json()
        lista_obiektow_brewery: List[Brewery] = []

        # Pętla po pobranych danych
        for wpis in dane_json:
            nowy_browar = Brewery(
                name=wpis.get("name", "Brak nazwy"),
                city=wpis.get("city", "Nieznane miasto"),
                state=wpis.get("state", "Brak stanu"),
                country=wpis.get("country", "Brak kraju"),
            )
            lista_obiektow_brewery.append(nowy_browar)

        # Wyświetlenie obiektów
        for browar in lista_obiektow_brewery:
            print(browar)
    else:
        print("Nie udało się połączyć z API")


if __name__ == "__main__":
    pobierz_browary()
