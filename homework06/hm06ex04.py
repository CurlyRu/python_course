'''
4.Реализуйте базовый класс Car.
У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.

Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат.
'''


class Car():

    def __init__(self, color: str, name: str, speed: int, is_polise: bool):
        self.color = color
        self.name = name
        self.speed = speed
        self.is_polise = is_polise

    def go(self):
        return f"{self.color} {self.name} is going. The speed is >>> {self.speed} km/h"

    def stop(self):
        self.speed = 0
        return f"{self.color} {self.name} is stopped. The speed is >>> {self.speed} km/h"

    def turn(self, direction: str):
        return f"{self.color} {self.name} turned >>> {direction}"

    def show_speed(self):
        return f"{self.color} {self.name} is traveling at a speed >>> {self.speed} km/h"


class TownCar(Car):
    def __init__(self, color, name, speed, is_polise):
        super().__init__(color, name, speed, is_polise)

    def show_speed(self):
        super().show_speed()
        if self.speed > 60:
            return f"{self.color} {self.name} speed is >>> {self.speed} km/h >>> Warning! High speed!"
        else:
            return f"{self.color} {self.name} speed is >>> {self.speed} km/h >>> Allowed speed"


class SportCar(Car):
    def __init__(self, color, name, speed, is_polise):
        super().__init__(color, name, speed, is_polise)


class WorkCar(Car):
    def __init__(self, color, name, speed, is_polise):
        super().__init__(color, name, speed, is_polise)

    def show_speed(self):
        super().show_speed()
        if self.speed > 40:
            return f"{self.color} {self.name} speed is >>> {self.speed} km/h >>> Warning! High speed!"
        else:
            return f"{self.color} {self.name} speed is >>> {self.speed} km/h >>> Allowed speed"


class PoliceCar(Car):
    def __init__(self, color, name, speed, is_police):
        super().__init__(color, name, speed, is_police)


print(f"\n!!!TownCar!!!")
auto_tc = TownCar("White", "Seat", 50, False)
print(auto_tc.go(), auto_tc.turn('Right'), auto_tc.show_speed(), auto_tc.stop(), sep='\n')
print(f"Status police >>> {auto_tc.is_polise}")

print(f"\n!!!SportCar!!!")
auto_sc = SportCar("Red", "Porsche", 200, False)
print(auto_sc.go(), auto_sc.turn('Left'), auto_sc.show_speed(), auto_sc.stop(), sep='\n')

print(f"\n!!!WorkCar!!!")
auto_wc = WorkCar("Black", "Audi", 90, False)
print(auto_wc.go(), auto_wc.turn('Turn around'), auto_wc.show_speed(), auto_wc.stop(), sep='\n')

print(f"\n!!!PoliceCar!!!")
auto_pc = WorkCar("Blue", "Skoda", 100, True)
print(auto_pc.go(), auto_pc.turn('Right'), auto_pc.show_speed(), auto_pc.stop(),
      f'Status police >>> {auto_pc.is_polise}', sep='\n')
