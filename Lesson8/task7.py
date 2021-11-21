class ComplexNumber:

    def __init__(self, input_string):
        list_of_part = input_string.split()
        if list_of_part[2] == 'i':
            list_of_part[2] = "1i"
        self.imaginary = int(list_of_part[2][:-1]) if list_of_part[1] == '+' else int(f"-{list_of_part[2][:-1]}")
        self.real = int(list_of_part[0])

    def __add__(self, other):
        real_output = self.real + other.real
        imaginary_output = self.imaginary + other.imaginary
        if imaginary_output < 0:
            return f"{real_output} - {str(imaginary_output)[1:]}i"
        elif imaginary_output > 0:
            return f"{real_output} + {imaginary_output}i"
        elif imaginary_output == 0:
            return f"{real_output}"

    def __mul__(self, other):
        real_output = self.real * other.real - self.imaginary * other.imaginary
        imaginary_output = self.real * other.imaginary + other.real * self.imaginary
        if imaginary_output < 0:
            return f"{real_output} - {str(imaginary_output)[1:]}i"
        elif imaginary_output > 0:
            return f"{real_output} + {imaginary_output}i"
        elif imaginary_output == 0:
            return f"{real_output}"


cn01 = ComplexNumber("-1 + i")
cn02 = ComplexNumber("2 + 2i")

print(cn01 + cn02)
print(cn01 * cn02)
