'''
7. Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая строка должна содержать данные о фирме:
название, форма собственности, выручка, издержки.

Пример строки файла: firm_1 ООО 10000 5000.

Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
Если фирма получила убытки, в расчет средней прибыли ее не включать.

Далее реализовать список.
Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
Если фирма получила убытки, также добавить ее в словарь (со значением убытков).

Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].

Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:

[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
'''

import json

profit = {}
pr = {}
prof, prof_aver, i = 0, 0, 0
with open("text_7.txt", "r", encoding='utf-8') as file:
    for line in file:
        name, firm, finance, loss = line.split()
        profit[name] = int(finance) - int(loss)
        if profit.setdefault(name) >= 0:
            prof = prof + profit.setdefault(name)
            i += 1
    if i != 0:
        prof_aver = prof / i
        print(f'Average profit >>> {prof_aver:.3f}')
    else:
        print(f'Loss for all companies')
    pr = {'average profit': round(prof_aver)}
    profit.update(pr)
    print(f'Profit by company >>> {profit}')

with open('text_7.json', 'w', encoding='utf-8') as my_js:
    json.dump(profit, my_js)

    js_str = json.dumps(profit)
    print(f'Save statistic for JSON file >>> {js_str}')
