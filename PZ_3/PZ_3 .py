#Дан список размера N. Найти количество участков, на которых его элементы
#монотонно возрастают.

lst = []

for n in range(10):
    k = int(input(f"Введите число {n + 1}: "))
    lst.append(k)

count = 0
start = 0

for i in range(1, len(lst)):
    if lst[i] <= lst[i - 1]:
        count += 1
        start = i

# Добавляем 1 для последнего участка, если он возрастает
if start != len(lst) - 1:
    count += 1

print(f"Количество участков монотонного возрастания: {count}")