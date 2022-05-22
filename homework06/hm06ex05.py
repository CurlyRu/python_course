'''
5. Реализовать класс Stationery (канцелярская принадлежность).
Определить в нем атрибут title (название) и метод draw (отрисовка).
Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
В каждом из классов реализовать переопределение метода draw. Для каждого из классов метод должен выводить уникальное сообщение.
Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
'''


class Stationery():

    def __init__(self, titel: str):
        self.titel = titel

    def draw(self):
        print("Start of rendering:")


class Pen(Stationery):
    def __init__(self, titel):
        super(Pen, self).__init__(titel)

    def draw(self):
        print(f"Use a pen >>> {self.titel}")


class Pencil(Stationery):
    def __init__(self, titel):
        super(Pencil, self).__init__(titel)

    def draw(self):
        print(f"Use a pencil >>> {self.titel}")


class Handle(Stationery):
    def __init__(self, titel):
        super(Handle, self).__init__(titel)

    def draw(self):
        print(f"Use a handle >>> {self.titel}")


my_stat = Stationery(" ")
my_stat.draw()

my_pen = Pen("Parker")
my_pen.draw()

my_pencil = Pencil("Koh-i-Noor")
my_pencil.draw()

my_handle = Handle("Chartpak")
my_handle.draw()
