"""
Для задачи из блока 1 создать две функции, save_def и
load_def, которые позволяют сохранять информацию из
экземпляров класса (3 шт.) в файл и загружать ее
обратно. Использовать модуль pickle для сериализации и
десериализации объектов Python в бинарном формате.
"""

import pickle

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

student_1 = Student("Ирина", "Лебедева", [5, 5, 5, 5, 5])
student_2 = Student("Иван", "Петров", [5, 4, 5, 4, 4])
student_3 = Student("Антон", "Сидоров", [3, 4, 3, 5, 4])

with open("student.pkl", "wb") as file:
    pickle.dump(student_1, file)
    pickle.dump(student_2, file)
    pickle.dump(student_3, file)

with open("student.pkl", "rb") as file:
    student_1 = pickle.load(file)
    student_2 = pickle.load(file)
    student_3 = pickle.load(file)

print(student_1.__dict__)
print(student_2.__dict__)
print(student_3.__dict__)
