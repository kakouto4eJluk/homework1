my_list = list(input("Впишите любые символы: "))
print(my_list)
n = 0

if len(my_list) % 2:
    z = my_list[len(my_list) - 1]
    my_list.pop(len(my_list) - 1)
    while n < len(my_list):
        my_list.insert(n, my_list[n + 1])
        my_list.pop(n + 2)
        n += 2
    my_list += z
else:
    while n < len(my_list):
        my_list.insert(n, my_list[n + 1])
        my_list.pop(n + 2)
        n += 2

print(my_list)
