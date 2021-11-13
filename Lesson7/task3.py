class Cell:

    def __init__(self, number_of_boxes):
        self.number_of_boxes = number_of_boxes

    def __add__(self, other):
        # Объединение двух клеток. При этом число ячеек общей клетки должно равняться сумме ячеек исходных двух клеток.
        return Cell(self.number_of_boxes + other.number_of_boxes)

    def __sub__(self, other):
        substraction_result = self.number_of_boxes - other.number_of_boxes
        if substraction_result > 0:
            return Cell(self.number_of_boxes - other.number_of_boxes)
        else:
            return ("Вычесть ячейки не получится.")

    def __mul__(self, other):
        return Cell(self.number_of_boxes * other.number_of_boxes)

    def __truediv__(self, other):
        return Cell(round(self.number_of_boxes // other.number_of_boxes))

    def make_order(self, number_per_row):
        return f"*****\n*****\n*****"

cell01 = Cell(20)
cell02 = Cell(11)

cell03 = cell01 + cell02

cell03.make_order()