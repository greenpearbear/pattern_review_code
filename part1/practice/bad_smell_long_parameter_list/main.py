# У нас есть какой-то unit, которому мы в параметры передаем
# - наше игровое поле
# - х координату
# - у координаты
# - направление смещения
# - летит ли он
# - крадется ли он
# - скорость
# В этом примере есть сразу несколько запахов плохого кода. Исправьте их
#   (длинный метод, длинный список параметров)


class Unit:
    def __init__(self, field, x_coord, y_coord, direction, is_fly, crawl):
        self.field = field
        self.x_coord = x_coord
        self.y_coord = y_coord
        self.direction = direction
        self.is_fly = is_fly
        self.crawl = crawl
        self.speed = 1

    def _check_is_fly_and_crawl(self):
        if self.is_fly and self.crawl:
            raise ValueError('Рожденный ползать летать не должен!')

    def _choice_speed(self):
        if self.is_fly:
            self.speed *= 1.2
        elif self.crawl:
            self.speed *= 0.5
        else:
            raise ValueError('Что ты такое?')

    def _move(self):
        self._choice_speed()
        if self.direction == 'UP':
            self.field.set_unit(y=self.y_coord + self.speed, x=self.x_coord, unit=self)
        elif self.direction == 'DOWN':
            self.field.set_unit(y=self.y_coord - self.speed, x=self.x_coord, unit=self)
        elif self.direction == 'LEFT':
            self.field.set_unit(y=self.y_coord, x=self.x_coord - self.speed, unit=self)
        elif self.direction == 'RIGHT':
            self.field.set_unit(y=self.y_coord, x=self.x_coord + self.speed, unit=self)

    def lets_go(self):
        self._check_is_fly_and_crawl()
        self._move()
