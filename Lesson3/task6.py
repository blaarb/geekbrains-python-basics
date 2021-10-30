# В программу должна попадать строка из слов, разделенных пробелом.
# Каждое слово состоит из латинских букв в нижнем регистре.
# Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы.
# Необходимо использовать написанную ранее функцию int_func().

def int_func(input_string):
    return input_string.title()


result_string = ''
input_string = input("Введите строку из слов, разделенных пробелом.\n")
for substring in input_string.split():
    result_string += int_func(substring) + " "

print(f"{result_string}")
