'''
2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
'''

with open("text_2.txt", "r") as my_file:
    lines = my_file.readlines()
    count_lines = len(lines)
    print(f'Count of lines in the file >>> {count_lines}')
    for line in range(count_lines):
        count_words = lines[line].split()
        print(f'In {line + 1} line >>> {len(count_words)} word(s))')
