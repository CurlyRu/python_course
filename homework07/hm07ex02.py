'''
2. Реализовать проект расчета суммарного расхода ткани на производство одежды.
Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры:
размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы:
для пальто (V/6.5 + 0.5), для костюма (2*H + 0.3).
Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.
'''


class Clothes:

    def __init__(self, param: int):
        self.param = param


class Coat(Clothes):

    @property
    def square(self):
        return self.param / 6.5 + 0.5


class Jacket(Clothes):

    @property
    def square(self):
        return 2 * self.param + 0.3


class Total(Clothes):

    def __init__(self, param: int, param_add: int):
        super().__init__(param)
        self.param = param
        self.param_add = param_add

    @property
    def square(self):
        return (self.param / 6.5 + 0.5) + (2 * self.param_add + 0.3)


my_size, my_heigth = 48, 180

my_coat = Coat(my_size)
my_jacket = Jacket(my_heigth)
my_total = Total(my_size, my_heigth)

print(f"Amount of fabric on the coat >>> {my_coat.square:.2f}")
print(f"\nAmount of fabric on the jacket >>> {my_jacket.square:.2f}")
print(f"\nTotal fabric amount >>> {my_total.square:.2f}")
