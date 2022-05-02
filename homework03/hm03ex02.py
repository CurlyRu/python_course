# 2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.

def info(name, sname, bday, city, email, phone):
    print(f"{name}, {sname}, {bday}, {city}, {email}, {phone}")


info(name="Lola", sname="First", bday=1969, city="Karaganda", email="LolaF@mail.kg", phone="4242")
