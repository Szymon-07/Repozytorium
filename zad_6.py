def przetworz_listy(lista1: list, lista2: list) -> list:
    # 1. Łączenie list
    polaczona = lista1 + lista2

    # 2. Usuwanie duplikatów (konwersja na zbiór/set i z powrotem na listę)
    unikalna = list(set(polaczona))

    # 3. Potęgowanie do 3 stopnia (lista składana)
    wynik = [x ** 3 for x in unikalna]

    return wynik


# Testy
l1 = [1, 2, 2]
l2 = [2, 3, 4]
# Połączenie: [1, 2, 2, 2, 3, 4]
# Unikalne: [1, 2, 3, 4] (kolejność może być losowa w secie)
# Wynik (do potęgi 3): [1, 8, 27, 64]

print(przetworz_listy(l1, l2))