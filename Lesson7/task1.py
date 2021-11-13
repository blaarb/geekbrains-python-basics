class Matrix:
    def __init__(self, input_list):
        self.input_list = input_list

    def __str__(self):
        result_string = ''
        for list_element in self.input_list:
            result_string += str(f"{list_element}\n")
        return result_string

    def __add__(self, other):
        for i in range(len(self.input_list))

m1 = Matrix([[1, 2, 3], [4, 5, 6]])
m2 = Matrix([[7, 8, 9], [1, 2, 3]])

print(m1)

print([4, 5, 6] + [4, 5, 6])