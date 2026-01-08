from typing import List
from zad_1 import Student


class Library:
    def __init__(
        self, city: str, street: str, zip_code: str, open_hours: str, phone: str
    ):
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.open_hours = open_hours
        self.phone = phone

    def __str__(self):
        return f"Biblioteka: {self.city}, ul. {self.street}"


class Employee:
    def __init__(
        self,
        first_name: str,
        last_name: str,
        hire_date: str,
        birth_date: str,
        city: str,
        street: str,
        zip_code: str,
        phone: str,
    ):
        self.first_name = first_name
        self.last_name = last_name
        self.hire_date = hire_date
        self.birth_date = birth_date
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.phone = phone

    def __str__(self):
        return f"Pracownik: {self.first_name} {self.last_name}"


class Book:
    def __init__(
        self,
        library: Library,
        publication_date: str,
        author_name: str,
        author_surname: str,
        number_of_pages: int,
    ):
        self.library = library
        self.publication_date = publication_date
        self.author_name = author_name
        self.author_surname = author_surname
        self.number_of_pages = number_of_pages

    def __str__(self):
        return (
            f"Książka: {self.author_name} {self.author_surname} ({self.library.city})"
        )


class Order:
    def __init__(
        self, employee: Employee, student: Student, books: List[Book], order_date: str
    ):
        self.employee = employee
        self.student = student
        self.books = books
        self.order_date = order_date

    def __str__(self):
        books_str = ", ".join([f"{b.author_surname}" for b in self.books])
        return f"Zamówienie ({self.order_date}): Student {self.student.name}, Pracownik {self.employee.last_name}, Książki: [{books_str}]"


if __name__ == "__main__":
    lib1 = Library("Warszawa", "Marszałkowska 1", "00-001", "8-16", "111-222-333")
    lib2 = Library("Kraków", "Floriańska 2", "30-001", "9-17", "444-555-666")

    emp1 = Employee(
        "Jan",
        "Kowalski",
        "2020-01-01",
        "1990-05-05",
        "Warszawa",
        "Polna",
        "00-002",
        "111",
    )
    emp2 = Employee(
        "Anna", "Nowak", "2021-06-01", "1995-10-10", "Kraków", "Leśna", "30-002", "222"
    )
    emp3 = Employee(
        "Piotr",
        "Wiśniewski",
        "2022-03-15",
        "1998-12-12",
        "Gdańsk",
        "Morska",
        "80-001",
        "333",
    )

    stud1 = Student("Marek", [3, 4, 5])
    stud2 = Student("Kasia", [5, 5, 5])
    stud3 = Student("Tomek", [2, 2, 3])

    b1 = Book(lib1, "2000", "Adam", "Mickiewicz", 300)
    b2 = Book(lib1, "2005", "Henryk", "Sienkiewicz", 400)
    b3 = Book(lib2, "2010", "Juliusz", "Słowacki", 250)
    b4 = Book(lib2, "2020", "Remigiusz", "Mróz", 350)
    b5 = Book(lib1, "1999", "Bolesław", "Prus", 600)

    order1 = Order(emp1, stud1, [b1, b2], "2023-12-01")
    order2 = Order(emp2, stud2, [b3, b4, b5], "2023-12-02")

    print(order1)
    print(order2)
