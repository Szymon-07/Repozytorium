from typing import List


class Student:
    def __init__(self, name: str, marks: List[int]):
        self.name = name
        self.marks = marks

    def is_passed(self) -> bool:
        if not self.marks:
            return False
        # Obliczanie średniej
        average = sum(self.marks) / len(self.marks)
        # Zwraca True jeśli średnia > 50, inaczej False
        return average > 50


# Testowanie (zgodnie z poleceniem: jeden zdaje, drugi nie)
student_zdal = Student("Ania", [60, 70, 80])
student_oblal = Student("Tomek", [30, 40, 40])

print(f"Student {student_zdal.name} zdał: {student_zdal.is_passed()}")
print(f"Student {student_oblal.name} zdał: {student_oblal.is_passed()}")
