# 3. Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.

month = int(input("Введите номер месяца >>> "))
if 1 < month < 12:
    if month in [1, 2, 12]:
        print("Решение через список -", 'Winter')
    elif month in [3, 4, 5]:
        print("Решение через список -", 'Spring')
    elif month in [6, 7, 8]:
        print("Решение через список -", 'Summers')
    elif month in [9, 10, 11]:
        print("Решение через список -", 'Autumn')
else:
    print('Неверный номер месяца')

month_dict = {"Winter": [1, 2, 12], "Spring": [3, 4, 5], "Summer": [6, 7, 8], "Autumn": [9, 10, 11]}
for key, value in month_dict.items():
    if month in value:
        print("Решение через словарь -", key)
        break