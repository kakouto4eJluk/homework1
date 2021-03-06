'''
Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
'''

def div(arg1, arg2):

    try:
        res = arg1 / arg2
    except ZeroDivisionError:
        return print('При делении положительного числа на 0 вы получите положительную бесконечность.\nАналогичтно и с отрицательными.\nПриделении 0 на 0:\nПредставьте, что у вас ноль печенек и вы делите их равномерно среди нуля друзей.\nСколько печенек получит каждый человек? Видите? Это бессмысленно.\nИ Коржик грустит, потому что нет печенек. И вы грустите, потому что у вас нет друзей.')

    return res

def start():

    try:
        print(div(float(input('Введите первое число: ')), float(input('Введите второе число: '))))
    except ValueError:
        return print('Надо было ввести числа...'), start()

start()
