# 1. Создать список и заполнить его элементами различных типов данных.
# Реализовать скрипт проверки типа данных каждого элемента.
# Использовать функцию type() для проверки типа.
# Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.

my_list = ['hello', 1, 123.321, [9, 1, 5], False, None, tuple("1, 2, 3"), dict(key_1='val_1', key_2='val_2')]
print(my_list)
for _ in my_list:
    print(type(_))