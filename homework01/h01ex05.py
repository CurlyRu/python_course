# 5. Запросите у пользователя значения выручки и издержек фирмы.
# Определите, с каким финансовым результатом работает фирма (прибыль — выручка больше издержек, или убыток — издержки больше выручки).
# Выведите соответствующее сообщение. Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке).
# Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.

revenue = float(input("Введите выручку фирмы: "))
costs = float(input("Введите затраты фирмы: "))
if revenue > costs:
    print("Уху! У нас прибыль!!!", "Рентабельность равна: ", (revenue - costs) / revenue)
    size = int(input("Введите численность сотрудников фирмы: "))
    costs_person = revenue / size
    print("Прибыль фирмы в расчете на одного сотрудника равна ", costs_person)
else:
    print("У фирмы убыток!!!")