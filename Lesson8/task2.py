class ExampleException(Exception):

    def __init__(self, input_string):
        self.input_string = input_string


try:
    a = int(input("Введите делимое\n"))
    b = int(input("Введите делитель\n"))
except ValueError:
    print("Кажется Вы ввели одно из чисел неправильно")
    exit(1)

try:
    if b == 0:
        raise ExampleException("Вы пытаетесь делить на ноль!")
    else:
        print(f"Результат деления: {a / b}")
except ExampleException as error:
    print(error)
