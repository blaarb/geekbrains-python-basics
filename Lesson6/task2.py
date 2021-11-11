

class Road:
    _length = 0
    _width = 0

    def calculate_volume(self, cm_mass, thickness):
        return self._length * self._width * cm_mass * thickness


road01 = Road()
road01._length = 5000
road01._width = 20
print(road01.calculate_volume(25, 5))
