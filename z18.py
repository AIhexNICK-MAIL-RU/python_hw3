# Задача 18: Требуется найти в массиве A[1..N] самый 
# близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное 
# число N – количество элементов в массиве. В последующих  
# строках записаны N целых чисел Ai. Последняя строка
# содержит число X

# *Пример:*
# 5
# 1 2 3 4 5
# 6 -> 5

import random, math
print(
    'Задача вычисляет сколько раз содержится натуральное'
     'число Х в массиве из N натуральных чисел'
    )
def checkInputInt(s):
    p = (input(f'{s}'))
    while p.isdigit() != True or int(p) <= 0:
        print('Вы ввели нецелое положительное число')
        p = (input(f'{s}'))
    return int(p)
    
n = checkInputInt('Введите число элементов массива ')
list_1 = list()

for i in range(n):
    list_1.append(random.randint(0, 99))

print(f'сгенерирован массив {list_1}')

x = checkInputInt('Введите число для сравнения ')
closer = math.abs(list_1[0] - x)

for i in range(1, n):
    if math.abs(list_1[i] - x) < closer:
        closer = list_1[i]

print(f'к числу {x} ближайшее в массиве {closer}')