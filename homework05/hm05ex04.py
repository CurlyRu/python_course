'''
4. Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4

Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
'''

num_rus = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
new_list = []

with open("text_4.txt", "r", encoding="UTF-8") as my_file:
    for i in my_file:
        i = i.split(' ', 1)
        # print(i)
        new_list.append(num_rus[i[0]] + ' ' + i[1])
    print(f'Result >>> {new_list}')

with open("text_4_1.txt", "w", encoding="UTF-8") as my_file_1:
    my_file_1.writelines(new_list)
