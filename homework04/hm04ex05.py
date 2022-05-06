# 5. Реализовать формирование списка, используя функцию range() и возможности генератора.
# В список должны войти четные числа от 100 до 1000 (включая границы).
# Необходимо получить результат вычисления произведения всех элементов списка.
# Подсказка: использовать функцию reduce().


# Первый вариант решения
from functools import reduce

new_list = [el for el in range(100, 1001) if el % 2 == 0]
print(f"Первый вариант решения: четные числа в диапазоне от 100 до 1000: {new_list}")

def my_func(arg_1, arg_2):
    return arg_1 * arg_2

print(reduce(my_func, new_list))

print("\n")


# Второй вариант решения (через lambda)
from functools import reduce

new_list = [el for el in range(100, 1001) if el % 2 == 0]
print(f"Второй вариант решения: четные числа в диапазоне от 100 до 1000 >>> {new_list}")
total = reduce(lambda z, x: z * x, new_list)
print(f"Второй вариант решения: произведение четных чисел в диапазоне от 100 до 1000 >>> {total}")
