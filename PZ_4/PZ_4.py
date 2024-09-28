#Дано целое число N (>0) и символ C. Вывести строку длины N, которая состоит из
#символов C.

N = int(input('Введите число: '))
C = input('Введите символ: ')

result = ''

for i in range(N):
    result += C
print(result)
