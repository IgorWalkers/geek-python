# Запросите у пользователя значения выручки и издержек фирмы. Определите,
# с каким финансовым результатом работает фирма (прибыль — выручка больше издержек,
# или убыток — издержки больше выручки). Выведите соответствующее сообщение.
# Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке).
# Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.
earnings = float(input("Введите выручку фирмы >>> "))
expenses = float(input("Введите издержки фирмы >>> "))

if earnings > expenses:
    gross = earnings - expenses
    print(f"Фирма прибыльная. Валовая прибыль предприятия: {gross}")
    humans = int(input("Введите численность сотрудников >>> "))
    print("Прибыль фирмы в расчете на каждого сотрудника составила:", round(gross / humans, 2))
else:
    print("Фирмы убыточная")
