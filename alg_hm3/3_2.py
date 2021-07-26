'''2. Во втором массиве сохранить индексы чётных элементов первого
массива. Например, если дан массив со значениями 8, 3, 15, 6, 4, 2, то
во второй массив надо заполнить значениями 1, 4, 5, 6 (или 0, 3, 4, 5 -
если индексация начинается с нуля), т.к. именно в этих позициях первого
массива стоят чётные числа.'''

import random

r = [random.randint(0, 99) for _ in range(10)]
print(f'Первый массив {r}.')
index_even = []

for n in r:
    if n % 2 == 0:
        index_even.append(r.index(n))

print(f'Индексы чётных элементов первого массива: {index_even}.')
