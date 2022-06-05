'''
Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число, месяц, год и
преобразовывать их тип к типу «Число».
Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
Проверить работу полученной структуры на реальных данных.
'''


class Data:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    @classmethod
    def int_date(cls, data):
        d, m, y = data.split('-')
        return cls(int(d), int(m), int(y))

    @staticmethod
    def valid_date(date):
        if date.day < 1 or date.day > 31:
            return "Day must be within 1...31"
        elif date.month > 12 or date.month < 1:
            return "Month must be within 1...12"
        elif date.year < 1:
            return "Year must be more 0"
        else:
            return f"Valid date >>> {date.day}-{date.month}-{date.year}"


my_date = Data.int_date("04-06-2022")
print(Data.valid_date(my_date))
my_date = Data.int_date("00-06-2022")
print(Data.valid_date(my_date))
my_date = Data.int_date("04-00-2022")
print(Data.valid_date(my_date))
my_date = Data.int_date("04-12-0")
print(Data.valid_date(my_date))
my_date = Data.int_date("19-11-1195")
print(Data.valid_date(my_date))
