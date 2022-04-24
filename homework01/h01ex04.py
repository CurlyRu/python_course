# 4. Пользователь вводит целое положительное число.
# Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.

num_in = int(input("Введите целое положительное число: "))
a = 0
maximum_1 = 0
while num_in != 0:
    maximum = num_in % 10
    if maximum_1 < maximum:
        maximum_1 = maximum
    num_in = num_in // 10
print(f'Самая большая цифра в числе: {maximum_1}')