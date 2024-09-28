"""
Организовать и вывести последовательность А из n чисел. Из
последовательности А получить две последовательности В и С:
в последовательности В – четные элементы А, в С – нечетные
элементы А. Произвести суммирование соответствующих элементов
последовательностей В и С. Найти минимальный элемент полученной
последовательности.
"""
import random

list_a = [random.randint(1, 100) for i in range(1, 11)]

list_b = list(filter(lambda x: x % 2 == 0, list_a))
list_c = list(filter(lambda x: x % 2 != 0, list_a))

result = [a + b for a, b in zip(list_b, list_c)]

min_el = min(result)

print(f"Список A: {list_a}")
print(f"Список B с чётными числами: {list_b}")
print(f"Список C с нечётными числами: {list_c}")
print(f"Сумма соответствующих элементов списков A и B: {result}")
print(f"Минимальный элемент списка: {min_el}")
