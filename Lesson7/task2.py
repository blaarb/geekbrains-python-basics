from abc import ABC, abstractmethod


class Clothes(ABC):

    @abstractmethod
    def calc_volume(self):
        pass


class Coat(Clothes):

    def __init__(self, size):
        self.size = size

    @property
    def calc_volume(self):
        return self.size / 6.5 + 0.5


class Costume(Clothes):

    def __init__(self, height):
        self.height = height

    @property
    def calc_volume(self):
        return 2 * self.height + 0.3


costume1 = Costume(20)
print(costume1.calc_volume)

coat1 = Coat(20)
print(coat1.size)
