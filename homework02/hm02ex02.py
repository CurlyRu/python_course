# 2. Для списка реализовать обмен значений соседних элементов.
# Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().

value = input("Введите элементы списка через разделитель 'пробел' >>> ").split()
i = 0
my_list = list(value)
print(my_list)
quantity_list = len(my_list) # длина списка
print("Количество элементов в списке:", quantity_list)

if quantity_list % 2 == 0:  # если количество элементов в списке ЧЕТНОЕ число
    while i < quantity_list:
        my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
        i += 2
    print(my_list)
else:                       # если количество элементов в списке НЕЧЕТНОЕ число
    while i < quantity_list - 2: # уменьшили список на 2 последних элемента
        my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
        i += 2
    my_list[quantity_list - 2] = my_list[quantity_list-1]
    print(f'Результат решения:', my_list)
