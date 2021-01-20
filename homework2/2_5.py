my_list = [7, 5, 3, 3, 2]
print(f"Рейтинг - {my_list}")
digit = input("Введите новый элемент рейтинга или 'End' чтобы закончить: ")

while True:
    if digit.isnumeric():
        digit = int(digit)
        break
    else:
        digit = str(digit)
        if digit != 'End':
            digit = input("Введите новый элемент рейтинга или 'End' чтобы закончить: ")
        else:
            break


while digit != 'End':
    my_list.append(digit)
    my_list.sort()
    my_list.reverse()
    print(f"текущий список - {my_list}")
    digit = input("Введите новый элемент рейтинга или 'End' чтобы закончить: ")
    while True:
        if digit.isnumeric():
            digit = int(digit)
            break
        else:
            digit = str(digit)
            if digit != 'End':
                digit = input("Введите новый элемент рейтинга или 'End' чтобы закончить: ")
            else:
                break
