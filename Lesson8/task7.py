class ComplexNumber:

    def __init__(self, input_string):
        list_of_parts = input_string.split()
        list_of_parts[2] = list_of_parts[2][:-1]
        print(list_of_parts)
        self.imaginary = int(list_of_parts[2])
        self.real = int(list_of_parts[0])

    def __add__(self, other):
        real_output = self.real + other.real
        imaginary_output = self.imaginary + other.imaginary
        return f"{real_output} + {imaginary_output}i"


cn01 = ComplexNumber("5 + 6i")
cn02 = ComplexNumber("-3 + 2i")

print(cn01 + cn02)
