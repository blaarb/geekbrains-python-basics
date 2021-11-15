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
            return "Вычесть ячейки не получится."

    def __mul__(self, other):
        return Cell(self.number_of_boxes * other.number_of_boxes)

    def __truediv__(self, other):
        return Cell(round(self.number_of_boxes / other.number_of_boxes))

    def make_order(self, boxes_per_row):
        number_of_rows = self.number_of_boxes // boxes_per_row
        output_string = ''
        cellbox_string = '*'
        for i in range(number_of_rows):
            output_string += f"{boxes_per_row * cellbox_string}\n"

        output_string += f"{(self.number_of_boxes % boxes_per_row) * cellbox_string}"
        return output_string


cell01 = Cell(20)
cell02 = Cell(11)

# cell03 = cell01 + cell02
# print(cell03.make_order(5))

# cell04 = cell01 - cell02
# print(cell04.make_order(5))

# cell05 = cell02 - cell01
# print(cell05)

# cell06 = cell01 * cell02
# print(cell06.make_order(10))

cell07 = cell01 / cell02
print(cell07.make_order(1))
