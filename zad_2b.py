# Wersja 1: Pętla for
def pomnoz_przez_dwa_v1(lista_liczb):
    wynik = []
    for liczba in lista_liczb:
        wynik.append(liczba * 2)
    return wynik


# Wersja 2: Lista składana
def pomnoz_przez_dwa_v2(lista_liczb):
    return [liczba * 2 for liczba in lista_liczb]


# Testowanie
liczby = [1, 2, 3, 4, 5]

print("Oryginalna lista:", liczby)
print("Wersja pętla for:", pomnoz_przez_dwa_v1(liczby))
print("Wersja lista składana:", pomnoz_przez_dwa_v2(liczby))
