# Вариант 8: Дан размер файла в байтах. Используя операцию деления деления нацело,
# найти количество полных килобайтов, которые занимает данный файл (1 килобайт = 1024 байта).
size = int(input('Write size of the file in bytes: '))
size = size // 1024
print('The size of the file in Kbytes is: ', size)