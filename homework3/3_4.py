'''
Программа принимает действительное положительное число x и целое отрицательное число y.
Необходимо выполнить возведение числа x в степень y.
Задание необходимо реализовать в виде функции my_func(x, y).
При решении задания необходимо обойтись без встроенной функции возведения числа в степень.

Подсказка: попробуйте решить задачу двумя способами.
Первый — возведение в степень с помощью оператора **.
Второй — более сложная реализация без оператора **, предусматривающая использование цикла.
'''

def my_fync(x, y):
    z = x
    w = abs(y)
    for i in range(0, w - 1):
        x *= z
    if y > 0:
        print(f'{z} в степени {y} равен {x}')
    elif y < 0:
        print(f'{z} в степени {y} равен 1/{x}')
    elif y == 0:
        print(f'Любое число в нулевой степени равно 1')

'''
x это число которое вы возводим в степень y
w модуль от y(так легче считать)
z это число которое мы изначально возводим в степень(x)
'''

my_fync(int(input('Введите первое число: ')), int(input('Введите второе число: ')))