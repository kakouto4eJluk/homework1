'''
Реализовать функцию, принимающую несколько параметров,
описывающих данные пользователя: имя, фамилия, год рождения,
город проживания, email, телефон. Функция должна принимать
параметры как именованные аргументы. Реализовать вывод данных
о пользователе одной строкой.
'''

user_info = {'имя': '', 'фамилию': '', 'год рождения': '', 'email': '', 'телефон': ''}

'''
name = input('Введите имя: ')
surname = input('Введите фамилию: ')
year = int(input('Введите год рождения: '))
city = input('Введите город проживания: ')
email = input('Введите email: ')
telephone = input('Введите номер телефона: ')
'''
def my_func ():
    for f in user_info.keys():
        user_data = input(f'Введите {f}: ')
        user_info[f] = user_data
    print(user_info)


my_func()