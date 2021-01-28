'''
 Реализовать два небольших скрипта:
а) итератор, генерирующий целые числа, начиная с указанного,
б) итератор, повторяющий элементы некоторого списка, определенного заранее.
Подсказка: использовать функцию count() и cycle() модуля itertools.
Обратите внимание, что создаваемый цикл не должен быть бесконечным. Необходимо предусмотреть условие его завершения.
Например, в первом задании выводим целые числа, начиная с 3, а при достижении числа 10 завершаем цикл.
Во втором также необходимо предусмотреть условие, при котором повторение элементов списка будет прекращено.
'''

#a
from itertools import count
num = int(input('Введите стартовое число: '))

for el in count(num):
    if el <= num + 10: # Я указал на 10 чисел, но можно вписать любое условие
        print(el)
    else:
        break

'''
Если запустить через терминал то он дублирует числа(не знаю как пофиксить). Если просто Run нажить то пишет правильно.
'''

#б
from itertools import cycle
try_cycle = int(input('Количество повторов: '))
my_list = [True, 'Basil', 1337, None, 2]
len_try = 1

for el in cycle(my_list):
    if len_try <= try_cycle * len(my_list):
        len_try += 1
        print(el)
    else:
        break

'''
len_try - это переменная счётчик которая считает кол-во элементов которые напичатала программа.
'''
'''
for el in count(int(input('Введите стартовое число: '))):
    print(el)
        
Бесконечный вариант 1
-----------------------------------------------------------------------------------------------------------
my_list = [True, 'Basil', 1337, None, 2]
for el in cycle(my_list):
        print(el)

Бесконечный вариант 2
'''