# Узнайте у пользователя число n.
# Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.

number = input("Введите число >>> ")
count = 1
result = 0
while count <= 3:
    result += int(number * count)
    count += 1
print(f"Результат {result}")
