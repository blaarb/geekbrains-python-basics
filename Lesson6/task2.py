

class Road:
    _length = 20
    _width = 5000

    def calculate_volume(self, cm_mass, thickness):
        return self._length * self._width * cm_mass * thickness


road01 = Road()
print(road01.calculate_volume(25, 5))
