"""
Создайте класс «Студент», который имеет атрибуты имя,
фамилия и оценки. Добавьте методы для вычисления
среднего балла и определения, является ли студент
отличником.
"""

name = input("Введите имя: ")
surname = input("Введите фамилию: ")
a = []

for i in range(5):
    grades = int(input("Введите оценку: "))
    a.append(grades)

class Student:
    def __init__(self, first_name, last_name, grades):
        self.first_name = first_name
        self.last_name = last_name
        self.grades = grades

    def is_honor(self):
        average_grade = sum(self.grades) / len(self.grades)
        return average_grade == 5

    def __repr__(self):
        average_grade = sum(self.grades) / len(self.grades)
        return (f"Студент: {self.first_name} {self.last_name}""\n"
                f"Оценки: {self.grades}""\n"
                f"Средний балл: {average_grade}""\n"
                f"Отличник: {'Да' if average_grade == 5 else 'Нет'}")

print(Student(name, surname, a))
