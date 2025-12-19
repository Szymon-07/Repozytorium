import requests
import argparse
from typing import List, Optional


# --- Klasa Brewery (bez zmian) ---
class Brewery:
    def __init__(self, name: str, city: str, state: str, country: str):
        self.name = name
        self.city = city
        self.state = state
        self.country = country

    def __str__(self) -> str:
        return f"Browar: {self.name} | Lokalizacja: {self.city}, {self.state} ({self.country})"


# --- Funkcja pobierająca ---
def pobierz_browary(city: Optional[str] = None) -> None:
    url = "https://api.openbrewerydb.org/v1/breweries"

    # Parametry zapytania do API
    # per_page=20: pobierz 20 sztuk
    params = {'per_page': 20}

    # Jeśli podano miasto, dodaj filtr 'by_city' do zapytania
    if city:
        params['by_city'] = city
        print(f"--- Szukam browarów w mieście: {city} ---")
    else:
        print("--- Pobieram dowolne browary ---")

    try:
        # requests.get sam doklei parametry do adresu URL
        response = requests.get(url, params=params)

        if response.status_code == 200:
            dane_json = response.json()

            if not dane_json:
                print("Nie znaleziono żadnych browarów dla podanych kryteriów.")
                return

            lista_obiektow_brewery: List[Brewery] = []

            for wpis in dane_json:
                nowy_browar = Brewery(
                    name=wpis.get('name', 'Brak nazwy'),
                    city=wpis.get('city', 'Nieznane miasto'),
                    state=wpis.get('state', 'Brak stanu'),
                    country=wpis.get('country', 'Brak kraju')
                )
                lista_obiektow_brewery.append(nowy_browar)

            for browar in lista_obiektow_brewery:
                print(browar)
        else:
            print(f"Błąd API: {response.status_code}")

    except Exception as e:
        print(f"Wystąpił błąd połączenia: {e}")


# --- Główna część z argparse ---
if __name__ == '__main__':
    # Konfiguracja parsera argumentów
    parser = argparse.ArgumentParser(description="Pobieranie browarów z API")

    # Dodanie argumentu --city
    parser.add_argument('--city', type=str, help="Nazwa miasta do filtrowania (np. San_Diego)")

    # Odczytanie argumentów
    args = parser.parse_args()

    # Uruchomienie funkcji z przekazanym miastem (lub None)
    pobierz_browary(args.city)