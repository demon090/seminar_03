# Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N].
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

from random import randint

n = int(input('введите количество элементов:    '))
print(" ")
list = []
x = int(input('введите цифру от 1 до 9:     '))
print(" ")
count = 0

for i in range(n):
    list.append(randint(1,9))
    if list[i] == x:
        count += 1
    
print(f'массив:     {list}')
print(" ")
print(f'количество элементов:   {count}')
    