a = int(input("Введите результаты пробежки первого дня в км "))
b = int(input("Введите общий желаемый результат в км "))
result_days = 1
result_km = a
while result_km < b:
    result_km = result_km * 0.1 + result_km
    result_days += 1
print(f"Вы достигнете требуемых показателей на %.d день" % result_days)