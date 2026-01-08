def wypisz_parzyste(lista_liczb):
    print("Liczby parzyste:")
    for liczba in lista_liczb:
        # Operator % to reszta z dzielenia
        if liczba % 2 == 0:
            print(liczba)


# Wywołanie
lista_10_liczb = list(range(10))

# Uruchomienie funkcji
wypisz_parzyste(lista_10_liczb)
