"""
1) Перенести в новую матрицу matrix1 элементы, которые не
находятся в первых и последних строках и столбцах матрицы
matrix2 произвольного размера.
"""
# Импортируем бибилиотеку для генерации рандомных чисел
import random

# Создаём списки для взаимодействия с ними
matrix1 = []
matrix2 = []

# Делаем матрицу 4 на 4 из списка matrix2
for i in range(4):
    matrix2.append([random.randint(-10, 10) for j in range(4)])

"""
Из списка matrix2 достаём элементы, которые не находятся в первых и последних 
строках и столбцах матрицы matrix2
"""
for i in range(1, len(matrix2) - 1):
    matrix1.append([matrix2[i][j] for j in range(1, len(matrix2[0]) - 1)])

if __name__ == "__main__":
    # Выводим матрицу matrix2
    print("Матрица matrix2:")
    for value in matrix2:
        print(value)
    print()

# Выводим матрицу matrix1
print("Матрица matrix1:")
for value in matrix1:
    print(value)
print()
