'''
1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод init()),
который должен принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Следующий шаг — реализовать перегрузку метода str() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода add() для реализации операции сложения двух объектов класса Matrix (двух матриц).
Результатом сложения должна быть новая матрица.
'''


class Matrix:
    def __init__(self, my_list: list):
        self.mtx = my_list

    def __str__(self):
        return str('\n'.join(['\t'.join([str(elem) for elem in line]) for line in self.mtx]))

    def __add__(self, other):

        for i in range(len(self.mtx)):

            for j in range(len(other.mtx[i])):
                self.mtx[i][j] = self.mtx[i][j] + other.mtx[i][j]
        return Matrix.__str__(self)


mat_1 = Matrix([[1, 2, 3], [3, 2, 1], [4, 5, 6], [6, 5, 4]])
mat_2 = Matrix([[3, 2, 1], [1, 2, 3], [6, 5, 4], [4, 5, 6]])

print(mat_1)
print()
print(mat_2)
print(f"\n{mat_1.__add__(mat_2)}")
