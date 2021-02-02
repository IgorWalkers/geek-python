# Пользователь вводит целое положительное число.
# Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.
#
number = int(input("Введите целое, положительное цисло >>> "))
output_number = number  # для вывода изначального числа в конце
biggest = 0
remainder = 0  # остаток при делении на 10
while number > 0:
    remainder = number % 10
    if biggest < remainder:
        biggest = remainder
    number //= 10
print(f"Самая большая цифра в числе {output_number}: {biggest}")
