def czy_suma_wieksza(a: int, b: int, c: int) -> bool:
    # Zwraca wynik porównania (suma a i b vs c)
    return (a + b) >= c

# Testy
print(czy_suma_wieksza(2, 3, 4))  # 5 >= 4 -> True
print(czy_suma_wieksza(1, 1, 5))  # 2 >= 5 -> False