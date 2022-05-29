'''
Реализовать программу работы с органическими клетками, состоящими из ячеек.
Необходимо создать класс Клетка. В его конструкторе инициализировать параметр, соответствующий количеству ячеек клетки (целое число).
В классе должны быть реализованы методы перегрузки арифметических операторов:
сложение (__add__()),
вычитание (__sub__()),
умножение (__mul__()),
деление (__truediv__()).
Данные методы должны применяться только к клеткам и выполнять увеличение, уменьшение, умножение и целочисленное
(с округлением до целого) деление клеток, соответственно.
'''


class Cell:
    def __init__(self, quantity):
        self.quantity = quantity

    def __add__(self, other):
        return f"New big cell >>> {self.quantity + other.quantity}"

    def __sub__(self, other):
        sub = self.quantity - other.quantity
        return f"New little cell >>> {sub} " \
            if sub > 0 else "cell kaput!"

    def __truediv__(self, other):
        return f"Cell division >>> {self.quantity // other.quantity}"

    def __mul__(self, other):
        return f"Multiplication of cells >>> {self.quantity * other.quantity}"

    def make_order(self, row):
        result = ''
        for i in range(int(self.quantity / row)):
            result += '*' * row + '\n'
        result += '*' * (self.quantity % row) + '\n'
        return result


cell_one = Cell(20)
cell_two = Cell(12)
print(cell_one + cell_two)
print(cell_one - cell_two)
print(cell_one / cell_two)
print(cell_one * cell_two)
print(f"\nOrganize cells in rows:")
print(cell_one.make_order(8))
