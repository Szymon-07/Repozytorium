def czy_zawiera(lista: list, element: int) -> bool:
    # Operator 'in' sprawdza obecność elementu w kolekcji
    return element in lista


# Testy
moja_lista = [10, 20, 30, 40]
print(czy_zawiera(moja_lista, 30))  # True
print(czy_zawiera(moja_lista, 99))  # False
