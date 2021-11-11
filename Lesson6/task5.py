class Stationery:
    title = ''

    def draw(self):
        print("Запуск отрисовки.")


class Pen(Stationery):

    def draw(self):
        print("Письменная принадлежность для письма на бумаге жидкими чернилам.")


class Pencil(Stationery):

    def draw(self):
        print("Инструмент для рисования или черчения в виде грифеля в оправе, деревянной или пластиковой оболочке.")


class Handle(Stationery):

    def draw(self):
        print("Handle - это не маркер.")


pen01 = Pen()
pen01.title = "Ручка"
print(pen01.title)
pen01.draw()

pencil01 = Pencil()
pencil01.title = "Карандаш"
print(pencil01.title)
pencil01.draw()

handle01 = Handle()
handle01.title = "Не маркер"
print(handle01.title)
handle01.draw()
