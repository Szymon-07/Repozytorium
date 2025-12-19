# Funkcja zwraca True lub False (int -> bool)
def czy_parzysta(liczba: int) -> bool:
    # Operator % to reszta z dzielenia. Jeśli reszta z dzielenia przez 2 to 0, liczba jest parzysta
    return liczba % 2 == 0

# Testowanie
testowana_liczba = 7
wynik_logiczny = czy_parzysta(testowana_liczba)

# Wykorzystanie wyniku w warunku
if wynik_logiczny:
    print("Liczba parzysta")
else:
    print("Liczba nieparzysta")