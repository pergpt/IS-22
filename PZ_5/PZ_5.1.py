# Ваант 8: Даны два целых числа: А, В. Проверить истинность высказывания: «Каждое из чисел
# АиВ нечетное»
a = int(input())
b = int(input())
if a % 2 != 0 and b % 2 != 0:
    print("Не чётные")
else:
    print("Чётные")