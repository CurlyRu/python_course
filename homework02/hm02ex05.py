# 5. Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
# У пользователя необходимо запрашивать новый элемент рейтинга.
# Если в рейтинге существуют элементы с одинаковыми значениями, то новый элемент с тем же значением должен разместиться после них.
#
# Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
# Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
# Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
# Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.
#
# Набор натуральных чисел можно задать непосредственно в коде, например, my_list = [7, 5, 3, 3, 2].

my_list = [7, 5, 3, 3, 2]
num = int(input('Введите число: '))
quantity = my_list.count(num) # количество num в списке
print(quantity)
for el in my_list:
    if quantity > 0:
        position = my_list.index(num)  # первая позиция num в списке
        my_list.insert(position + quantity, num)
        print(my_list)
        break
    else:
        if num > el:
            el_ind = my_list.index(el)  # первая позиция el в списке
            my_list.insert(el_ind, num)
            break
        elif num < my_list[len(my_list) - 1]:
            my_list.append(num)
print(my_list)