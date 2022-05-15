'''
5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
'''


def sum_in_file():
    try:
        with open("text_5.txt", "w") as my_file:
            in_line = input('Enter the numbers >>> ')
            my_file.writelines(in_line)
            my_list = in_line.split()
            print(f'Entered data >>> {my_list}')
            my_sum = sum(map(int, my_list))
            print(f'Sum of numbers = {my_sum}')
    except (IOError, ValueError):
        print('Input/Output Error. Please, enter only numbers')


sum_in_file()
