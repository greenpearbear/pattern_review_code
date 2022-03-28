# Измените класс Person так, чтобы его методы 
# оперировали внутренним состоянием, 
# а не использовали цепочку вызовов объектов


class Person:
    def __init__(self, city_population, room_num):
        self.city_population = city_population
        self.room_num = room_num

    @property
    def get_person_room(self):
        return self.room_num

    @property
    def get_city_population(self):
        return self.city_population


# TODO после выполнения задания попробуйте
person = Person(1000000, 17)
print(person.get_person_room)
print(person.get_city_population)

