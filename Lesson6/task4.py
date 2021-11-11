import random


class Car:
    speed = 0
    color = None
    name = ""
    is_police = False
    fuel = random.randint(30, 100)

    def go(self):
        if self.speed == 0:
            self.speed += 10
            print("Машина поехала")
        else:
            self.speed += 10
            print("Машина ускорилась на 10 км/ч")

    def stop(self):
        if self.speed in range(0, 11):
            print("Машина остановилась.")
        else:
            self.speed -= self.speed
            print("Машина сбавила скорость на 10 км/ч.")

    def turn(self, direction):
        direction_eng_ru = {"left": "налево", "right": "направо"}
        print(f"Машина повернула {direction_eng_ru.get(direction)}")

    def show_speed(self):
        print(f"Текущая скорость машины: {self.speed} км/ч.")

class TownCar(Car):

    def show_speed(self):
        if self.speed > 60:
            print("Превышение скорости!")
        else:
            print(f"Текущая скорость машины: {self.speed} км/ч.")

class SportCar(Car):
    pass

class WorkCar(Car):

    def show_speed(self):
        if self.speed > 40:
            print("Превышение скорости!")
        else:
            print(f"Текущая скорость машины: {self.speed} км/ч.")

class PoliceCar(Car):
    is_police = True

sport_car01 = SportCar()
sport_car01.color = "red"
print(f"Мы создали спорткар цвета {sport_car01.color}.")

sport_car01.show_speed()
sport_car01.go()
sport_car01.show_speed()
sport_car01.turn("left")
sport_car01.show_speed()
sport_car01.turn("right")
sport_car01.show_speed()
sport_car01.go()
sport_car01.stop()
sport_car01.show_speed()
sport_car01.stop()
sport_car01.show_speed()

town_car01 = TownCar()
town_car01.color = "green"
print(f"Мы создали автомобиль цвета {town_car01.color}.")
town_car01.go()
town_car01.show_speed()
town_car01.go()
town_car01.go()
town_car01.go()
town_car01.show_speed()
town_car01.go()
town_car01.go()
town_car01.show_speed()
town_car01.go()
town_car01.show_speed()

police_car01 = PoliceCar()
police_car01.color = "reb blue black"
print(f"Мы создали автомобиль цвета {police_car01.color}.")
if police_car01.is_police is True:
    print("Это полицейский автомобиль")