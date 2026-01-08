# Funkcja przyjmuje dwa stringi i zwraca stringa (str -> str)
def stworz_powitanie(name: str, surname: str) -> str:
    return f"Cześć {name} {surname}!"


# Wywołanie funkcji i przypisanie do zmiennej
wynik = stworz_powitanie("Jan", "Kowalski")

# Wyświetlenie wyniku
print(wynik)
