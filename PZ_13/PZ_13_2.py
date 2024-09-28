"""
2) В матрице отрицательные элементы возвести в квадрат.
"""

__import__("PZ_13_1")

from PZ_13_1 import matrix1

matrix1 = matrix1

"""
Проверяем матрицу matrix1 на наличие отрицательных элементов и 
возводим в степень 2
"""
for i in range(len(matrix1)):
    for j in range(len(matrix1[0])):
        if matrix1[i][j] < 0:
            matrix1[i][j] = matrix1[i][j] ** 2

# Выводим матрицу matrix1 с возведёнными во 2 степень отрицательными числами
print("Возводим отрицательные числа из matrix1 во вторую степень:")
for value in matrix1:
    print(value)
