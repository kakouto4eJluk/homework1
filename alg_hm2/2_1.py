'''1. Написать программу, которая будет складывать, вычитать, умножать или делить два числа.
Числа и знак операции вводятся пользователем. После выполнения вычисления программа не должна
завершаться, а должна запрашивать новые данные для вычислений. Завершение программы должно
выполняться при вводе символа '0' в качестве знака операции. Если пользователь вводит неверный
знак (не '0', '+', '-', '*', '/'), то программа должна сообщать ему об ошибке и снова запрашивать
знак операции. Также сообщать пользователю о невозможности деления на ноль, если он ввел 0 в качестве делителя.'''

while True:
    try:
        number1 = int(input('Введите первое число: '))
        number2 = int(input('Введите втоорое число: '))
        operation = input("Введите операцию ('+', '-', '*', '/') или 0 чтобы завершить: ")
    except ValueError:
        print('Неправильный ввод.')
        continue

    if operation == '0':
        break
    elif operation == '+':
        print(f'{number1} {operation} {number2} = {number1 + number2}')
    elif operation == '-':
        print(f'{number1} {operation} {number2} = {number1 - number2}')
    elif operation == '*':
        print(f'{number1} {operation} {number2} = {number1 * number2}')
    elif operation == '/':
        try:
            print(f'{number1} {operation} {number2} = {number1 / number2}')
        except ZeroDivisionError:
            print('Ошибка. Деление на ноль')
