"""
Создайте класс "Человек", который содержит информацию
о имени, возрасте и поле.
Создайте классы "Мужчина" и "Женщина", которые
наследуются от класса "Человек".
Каждый класс должен иметь метод, который выводит
информацию о поле объекта.
"""

class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

class Man(Person):
    def __init__(self, name, age):
        super().__init__(name, age, "Мужчина")

class Woman(Person):
    def __init__(self, name, age):
        super().__init__(name, age, "Женщина")

def input_person_data():
    name = input("Введите имя: ")
    age = int(input("Введите возраст: "))
    gender = input('Введите пол ("м" или "ж"): ').lower()
    return name, age, gender

def create_person(name, age, gender):
    if gender == "м":
        return Man(name, age)
    elif gender == "ж":
        return Woman(name, age)
    else:
        raise ValueError("Неправильно указан пол")

name, age, gender = input_person_data()
person = create_person(name, age, gender)

print(f"Данные: ({person.name}, {person.age}, {person.gender})")
