'''
Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
'''

def my_func(pos1, pos2, pos3):
    my_list = list()
    my_list.append(pos1)
    my_list.append(pos2)
    my_list.append(pos3)
    my_list.sort(reverse=True)
    res = my_list[0] + my_list[1]
    return res
'''
pos1 = int(input('Введите первое число: '))
pos2 = int(input('Введите второе число: '))
pos3 = int(input('Введите третье число: '))
'''
print(my_func(int(input('Введите первое число: ')), int(input('Введите второе число: ')), int(input('Введите третье число: '))))