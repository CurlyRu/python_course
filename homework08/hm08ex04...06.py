'''
4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
А также класс «Оргтехника», который будет базовым для классов-наследников.
Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определить параметры, общие для приведенных типов.
В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.

5. Продолжить работу над первым заданием.
Разработать методы, отвечающие за приём оргтехники на склад и передачу в определенное подразделение компании.
Для хранения данных о наименовании и количестве единиц оргтехники,а также других данных,
можно использовать любую подходящую структуру, например словарь.

6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
'''


class OfficeEquipment:

    def __init__(self, name, release, price, *args):
        self.name: str = name
        self.release: int = release
        self.price: float = price


class Printer(OfficeEquipment):
    def __init__(self, name, release, price):
        super().__init__(name, release, price)
        self.ink: int = 50
        print(f"Model: {self.name} \t Release: {self.release} age \t Price: {self.price} $")

    @property
    def how_namy_ink(self):
        print(f"Currently, in {self.name} >>> {self.ink} % ink")

    def update_ink(self, up_ink):
        try:
            self.ink = int(up_ink)
            if self.ink > 100 or self.ink < 0:
                raise ValueError
        except ValueError:
            print("Invalid value")
            pass
        else:
            print(f"Data updated. in {self.name} >>> {self.ink} % ink")


class Scaner(OfficeEquipment):
    def __init__(self, name, release, price):
        super().__init__(name, release, price)
        self.quality: int = 200
        print(f"Model: {self.name} \t Release: {self.release} age \t Price: {self.price} $")

    @property
    def viewing_quality(self):
        print(f"Currently, in {self.name} >>> {self.quality} ppi")

    def setting_quality(self, new_quality):
        try:
            self.quality = int(new_quality)
            if self.quality > 1200 or self.quality < 50:
                raise ValueError
        except ValueError:
            print("Invalid value")
            pass
        else:
            print(f"Data updated. in {self.name} >>> {self.quality} ppi")


class Xerox(OfficeEquipment):
    def __init__(self, name, release, price):
        super().__init__(name, release, price)
        self.paper: int = 0
        print(f"Model: {self.name} \t Release: {self.release} age \t Price: {self.price} $")

    @property
    def paper_request(self):
        print(f"Currently, in {self.name} >>> {self.paper} page")

    def update_paper(self, new_paper):
        try:
            self.paper = int(new_paper)
        except ValueError:
            print("Invalid value")
            pass
        else:
            print(f"Data updated. in {self.name} >>> {self.paper} page")


class Stockroom:
    def __init__(self, name):
        self.name = name
        self.printers_quantity = {}
        self.scaners_quantity = {}
        self.xerox_quantity = {}

    def add_object(self, *args):
        for obj in args:

            if type(obj) is Printer:
                try:
                    self.printers_quantity[obj.name].append(obj)
                except KeyError:
                    self.printers_quantity[obj.name] = [obj]
            elif type(obj) is Scaner:
                try:
                    self.scaners_quantity[obj.name].append(obj)
                except KeyError:
                    self.scaners_quantity[obj.name] = [obj]
            elif type(obj) is Xerox:
                try:
                    self.xerox_quantity[obj.name].append(obj)
                except KeyError:
                    self.xerox_quantity[obj.name] = [obj]
            else:
                print("Unregistered object")

    @staticmethod
    def amount(all_list):
        return sum([len(all_list[i]) for i in list(all_list.keys())])

    def total_quantity_printers(self):
        print(f"Total printers in stockroom >>> {self.amount(self.printers_quantity)}")

    def total_quantity_scanners(self):
        print(f"Total scanners in stockroom >>> {self.amount(self.scaners_quantity)}")

    def total_quantity_xerox(self):
        print(f"Total xerox in stockroom >>> {self.amount(self.xerox_quantity)}")


printer_hp = Printer("HP", 2020, 4599)
printer_kyocera = Printer("Kyocera", 2015, 2500)
printer_hp.how_namy_ink
printer_hp.update_ink(200)
printer_hp.update_ink(98)
print()

scaner_cannon = Scaner("Cannon", 2010, 5000)
scaner_ricoh = Scaner("Ricohn", 2019, 6500)
scaner_cannon.viewing_quality
scaner_cannon.setting_quality(5000)
scaner_cannon.setting_quality(1100)
print()

xerox_brother = Xerox("Brother", 2022, 9000)
xerox_pantum = Xerox("Pantum", 2018, 5200)
xerox_brother.paper_request
xerox_brother.update_paper(500)
xerox_brother.paper_request
print()

total = Stockroom("Room")
total.add_object(printer_hp, scaner_cannon, printer_kyocera, xerox_pantum, xerox_brother)
total.total_quantity_printers()
total.total_quantity_scanners()
total.total_quantity_xerox()
