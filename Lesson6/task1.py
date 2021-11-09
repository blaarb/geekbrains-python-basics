import time
from itertools import cycle


class TrafficLight:
    __color = ("red", "yellow", "green")
    __timecodes = (7, 2, 5)

    def running(self):
        for element in cycle(self.__color):
            print(element)
            time.sleep(self.__timecodes[self.__color.index(element)])


tl1 = TrafficLight()
tl1.running()
