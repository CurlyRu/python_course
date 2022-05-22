'''
2. Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
Значения данных атрибутов должны передаваться при создании экземпляра класса.
Атрибуты сделать защищенными.
Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
Использовать формулу: длина*ширина*масса асфальта для покрытия одного кв метра дороги асфальтом, толщиной в 1 см*число см толщины полотна. Проверить работу метода.
Например: 20м*5000м*25кг*5см = 12500 т
'''


class Road():
    _lenght: float
    _width: float

    def __init__(self, _lenght, _width):
        self._lenght = _lenght
        self._width = _width

    def _asphalt_mass(self):
        weight_asphalt = 25
        dist_asphalt = 5
        print(f"Required asphalt mass >>> {round(self._lenght * self._width * weight_asphalt * dist_asphalt / 1000)} t")


my_object = Road(20, 5000)
my_object._asphalt_mass()
