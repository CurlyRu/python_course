# 6. *Реализовать структуру данных «Товары».
# Она должна представлять собой список кортежей.
# Каждый кортеж хранит информацию об отдельном товаре.
# В кортеже должно быть два элемента — номер товара и словарь с параметрами
# (характеристиками товара: название, цена, количество, единица измерения).
# Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.
# Пример готовой структуры:

# [
#     (1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
#     (2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
#     (3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
# ]

# Необходимо собрать аналитику о товарах.
# Реализовать словарь, в котором каждый ключ — характеристика товара,
# например название, а значение — список значений-характеристик,
# например список названий товаров.


products = []
names = []
prices = []
counts = []
measures = []
for i in range(1, 3):
    print(f"Вводим информацию для {i}-го товара")
    name = input("Название: ")
    price = int(input("Цена: "))
    count = int(input("Количество: "))
    measure = input("Единица измерения: ")
    products.append((i, {'Название': name, 'Цена': price, 'Количество': count, 'ед': measure}))
print(f"Cписок товаров: {products}")

for i in products:
    names.append(i[1].get('Название'))
    prices.append(i[1].get('Цена'))
    counts.append(i[1].get('Количество'))
    measures.append(i[1].get('eд'))

report = {
    'Название': list(set(names)),
    'Цена': list(set(prices)),
    'Количество': list(set(counts)),
    'eд': list(set(measures))
}

print(f"Отчет по списку товаров: \n{report}")