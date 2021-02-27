'''
Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. Проверьте его работу на данных,
вводимых пользователем. При вводе пользователем нуля в качестве делителя программа должна корректно обработать
эту ситуацию и не завершиться с ошибкой.
'''


class DivisionByNull:
    def __init__(self, num):
        self.num = num

    @staticmethod
    def divide_by_null(num, num_2):
        try:
            return (num / num_2)
        except:
            if num == 0:
                return f'Представьте, что у вас ноль печенек и вы делите их равномерно среди нуля друзей.\nСколько печенек получит каждый человек? Видите? Это бессмысленно.\nИ Коржик грустит, потому что нет печенек. И вы грустите, потому что у вас нет друзей.\n'
            elif num > 0:
                return f'При делении положительного числа на 0 вы получите положительную бесконечность.\n'
            elif num < 0:
                return f'При делении отрицательного числа на 0 вы получите отрицательную бесконечность.\n'


div = DivisionByNull(21)
print(DivisionByNull.divide_by_null(21, 0))
print(DivisionByNull.divide_by_null(-21, 0))
print(DivisionByNull.divide_by_null(0, 0))
print(DivisionByNull.divide_by_null(21, 0.1))
print(div.divide_by_null(69, 0))
