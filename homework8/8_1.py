'''
Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число, месяц, год и
преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и
года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.
'''


class Data:

    def __init__(self, day_month_year):
        self.day_month_year = str(day_month_year)

    @classmethod
    def get_int_data(cls, day_month_year):
        my_date = []

        for i in day_month_year.split():
            if i != '-':
                my_date.append(i)

        return int(my_date[0]), int(my_date[1]), int(my_date[2])

    @staticmethod
    def valid(day, month, year):
        '''
        Это всё можно сильно сократить, но по скольку я  сильно задержал сдачу дз
        решил оставить рабочий черновой вариант.
        Тут проверяется високосный ли год, сколько дней в месяце + февраль.
        '''
        if month != 4 and month != 6 and month != 9 and month != 11:
            if year % 4 == 0:
                if month != 2:
                    if 1 <= day <= 31:
                        if 1 <= month <= 12:
                            if 2021 >= year >= 0:
                                return f'Верно!'
                            else:
                                return f'Неправильный год!'
                        else:
                            return f'Неправильный месяц!'
                    else:
                        return f'Неправильный день!'
                else:
                    if 1 <= day <= 29:
                        if 1 <= month <= 12:
                            if 2021 >= year >= 0:
                                return f'Верно!'
                            else:
                                return f'Неправильный год!'
                        else:
                            return f'Неправильный месяц!'
                    else:
                        return f'Неправильный день!'
            else:
                if month != 2:
                    if 1 <= day <= 31:
                        if 1 <= month <= 12:
                            if 2021 >= year >= 0:
                                return f'Верно!'
                            else:
                                return f'Неправильный год!'
                        else:
                            return f'Неправильный месяц!'
                    else:
                        return f'Неправильный день!'
                else:
                    if 1 <= day <= 28:
                        if 1 <= month <= 12:
                            if 2021 >= year >= 0:
                                return f'Верно!'
                            else:
                                return f'Неправильный год!'
                        else:
                            return f'Неправильный месяц!'
                    else:
                        return f'Неправильный день!'
        else:
            if 1 <= day <= 30:
                if 1 <= month <= 12:
                    if 2021 >= year >= 0:
                        return f'Верно!'
                    else:
                        return f'Неправильный год!'
                else:
                    return f'Неправильный месяц!'
            else:
                return f'Неправильный день!'

    def __str__(self):
        return f'Текущая указанная дата: {Data.get_int_data(self.day_month_year)}'


data = Data('04 - 11 - 1997')
print(data)
print(Data.valid(29, 2, 2021))
print(Data.valid(29, 13, 2020))
print(Data.get_int_data('31 - 01 - 2019'))
print(data.get_int_data('26 - 12 - 2021'))
print(Data.valid(29, 2, 2020))
