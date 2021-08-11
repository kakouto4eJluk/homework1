'''1. Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.'''

user_num = input('Введите трёхзначное число: ')

sum = 0
prod = 1

for f in user_num:
    sum += int(f)
    prod *= int(f)

print(f'Сумма цифр числа {user_num}: {sum}.')
print(f'Произведение цифр: {user_num}: {prod}.')
