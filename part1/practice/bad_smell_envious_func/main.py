# Вам не кажется, что CubeVolumeCalculator 
# чаще дергает методы класса Cube? Исправьте так, 
# чтобы избавиться от лишних обращений к классу Cube


class Cube:
    def __init__(self, x, y, z):
        self._x = x
        self._y = y
        self._z = z

    def calculate(self):
        return self._x * self._y * self._z


cube = Cube(2, 2, 2)
cube.calculate()
