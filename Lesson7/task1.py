import random


class Matrix:

    def __init__(self, input_list):
        self.list_of_lists = input_list

    def __str__(self):
        result_string = ''
        for list_element in self.list_of_lists:
            result_string += str(f"{list_element}\n")
        return result_string

    def __add__(self, other):
        result_matrix = []
        for i in range(len(self.list_of_lists)):
            result_row = []
            for j in range(len(self.list_of_lists[i])):
                result_row.append(self.list_of_lists[i][j] + other.list_of_lists[i][j])
            result_matrix.append(result_row)
        return result_matrix


m1 = Matrix([random.sample(range(1, 10), 3), random.sample(range(1, 10), 3), random.sample(range(1, 10), 3)])
m2 = Matrix([random.sample(range(1, 10), 3), random.sample(range(1, 10), 3), random.sample(range(1, 10), 3)])

print(m1)
print(m2)
print(m1 + m2)
