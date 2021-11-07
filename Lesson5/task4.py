# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.
import os

numbers_eng2ru = {
    "One": "Один",
    "Two": "Два",
    "Three": "Три",
    "Four": "Четыре",
    "Five": "Пять"
}


def get_russian_word(input_string):
    return numbers_eng2ru.get(input_string)


# os.remove("task4_output.txt")
file_to_erase = open("task4_output.txt", "w")
file_to_erase.close()

with open("task4.txt") as source_file:
    # print(source_file.encoding)
    for line in source_file:
        extracted_word = line.split()[0]
        numeral_number = line.split()[2]
        with open("task4_output.txt", "a") as output_file:
            print(source_file.encoding)
            output_file.write(f"{get_russian_word(extracted_word)} - {numeral_number}\n")
