# Даны два пелых числа А иВ (А < В). Найти сумму квадратов всех целых чисел от А
# до В включительно.

c = 0
a = int(input('Введите А: '))
b = int(input('Введите B: '))

for i in range(a, b+1):
    c = c + i**2
print('сумма квадратов всех целых чисел от А до В включительно', c)