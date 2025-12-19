def wypisz_co_drugi(lista_liczb):
    for i in range(0, len(lista_liczb), 2):
        print(lista_liczb[i])

# Wywołanie
lista_10_liczb = list(range(10))
wypisz_co_drugi(lista_10_liczb)