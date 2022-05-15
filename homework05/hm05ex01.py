'''
1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
'''

my_file = open("text_1.txt", "w")
while True:
    line = input("Enter data >>> ")
    if line:
        my_file.write(line + '\n')
    else:
        print("End the file")
        my_file.close()
        break
