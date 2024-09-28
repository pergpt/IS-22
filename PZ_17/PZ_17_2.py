"""
Задание предполагает, что у студента есть проект с
практическими работами (№2-№13), оформленный согласно
требованиям. Все задания выполняются c использованием
модуля OS:

1) перейдите в каталог PZ_11. Выведите список всех
файлов в этом каталоге. Имена вложенных подкаталогов
выводить не нужно.

2) Перейти в корень проекта, создать папку с именем
test. В ней создать еще одну папку test1. В папку test
переместить два файла из PZ_6, а в папку test1 - один
файл из PZ_7. Файл из PZ_7 переименовать в test.txt.
Вывести в консоль информацию о размере файлов в папке
test.

3) Перейти в папку с PZ_11, найти там файл с самым
коротким именем, имя вывести в консоль. Использовать
функцию basename () (os.path.basename()).

4) Перейти в любую папку где есть отчет в формате .pdf
и «запустите» файл в привязанной к нему программе.
Использовать функцию os.startfile().

5) Удалить файл test.txt.
"""

import os

# 1. Перейти в каталог PZ_11 и вывести список всех
# файлов в этом каталоге.
os.chdir("PZ_11")
files_in_pz11 = [f for f in os.listdir() if os.path.isfile(f)]
print("Список файлов в PZ_11:", files_in_pz11)

"""
2. Перейти в корень проекта, создать папку test и в 
ней папку test1. Переместить два файла из PZ_6 в test 
и один файл из PZ_7 в test1. Переименовать файл из 
PZ_7 в test.txt. Вывести размер файлов в папке test.
"""

# Переход в корень проекта
os.chdir("..")
# Создание папок test и test1
os.makedirs("test/test1", exist_ok=True)

# Перемещение файлов из PZ_6 в test
pz6_files = os.listdir("PZ_6")[:2]
for file in pz6_files:
    os.rename(f"PZ_6/{file}", f"test/{file}")

# Перемещение и переименование файла из PZ_7 в test1
pz7_file = os.listdir("PZ_7")[0]
os.rename(f"PZ_7/{pz7_file}", "test/test1/test.txt")

# Вывод информации о размере файлов в папке test
test_files = [f for f in os.listdir("test")
              if os.path.isfile(os.path.join("test", f))]
for file in test_files:
    print(f"Файл: {file}, Размер: "
          f"{os.path.getsize(os.path.join("test", file))} байт")

# 3. Перейти в папку PZ_11 и найти файл с самым
# коротким именем, имя вывести в консоль.
os.chdir("PZ_11")
shortest_file = min(files_in_pz11, key=len)
print("Файл с самым коротким именем в PZ_11:",
      os.path.basename(shortest_file))

"""
4. Перейти в любую папку, где есть отчет в формате .pdf 
и «запустить» файл в привязанной к нему программе. 
(Для примера, предположим, что PDF файл находится в 
папке PZ_8)
"""
os.chdir("../PZ_8")  # Переход в папку PZ_8
pdf_files = [f for f in os.listdir() if f.endswith(".pdf")]
if pdf_files:
    os.startfile(pdf_files[0])

# 5. Удалить файл test.txt.
os.remove("../test/test1/test.txt")
