# Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

from random import randint

n = int(input('Введите количество элементов:    '))
print(' ')
array = []
x = int(input('Вседите число от 1 до 9:     '))
print(' ')
number = 0

for i in range(n):
    array.append(randint(1,10))
    if x - array[i] < x - number and x - array[i] > 0:
        number = i

print(f'массив:     {array}')
print(' ')
print(array[number])