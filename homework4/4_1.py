'''
Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.


from argparse import ArgumentParser

try:
    parser = ArgumentParser()

    parser.add_argument('--output_in_hours', type=float)
    parser.add_argument('--rate_per_hour', type=float)
    parser.add_argument('--prize', type=float, default=1000)

    args = parser.parse_args()

    res = (args.output_in_hours * args.rate_per_hour) + args.prize
    print(res)
except ValueError:
    print('Надо было ввести числа.')

не ловит ошибку с буквами и я не понимаю почему
'''

from sys import argv

name, output_in_hours, rate_per_hour, prize = argv
try:
    output_in_hours = int(output_in_hours)
    rate_per_hour = int(rate_per_hour)
    prize = int(prize)
    res = output_in_hours * rate_per_hour + prize
    print(f'заработная плата сотрудника  {res}')
except ValueError:
    print('Надо было ввести числа.')
