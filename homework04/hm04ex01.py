# 1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
# В расчете необходимо использовать формулу: (выработка в часах*ставка в час) + премия.
# Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.



from sys import argv

my_script, production, bet, bonus = argv

def calculate_salary(production, bet, bonus):
    try:
        salary = (float(production) * float(bet)) + float(bonus)
        print(f"ЗП сотрудника составляет: {salary}")
    except ValueError:
        print("Внесены некорректные параметры")

calculate_salary(production, bet, bonus)