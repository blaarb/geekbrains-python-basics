# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

numbers_eng2ru = {
    "One": "Один",
    "Two": "Два",
    "Three": "Три",
    "Four": "Четыре",
    "Five": "Пять"
}

file_to_erase = open("task4_output.txt", "w")
file_to_erase.close()

with open("task4.txt") as source_file:
    for line in source_file:
        extracted_word = line.split()[0]
        numeral_number = line.split()[2]
        with open("task4_output.txt", "a") as output_file:
            output_file.write(f"{numbers_eng2ru.get(extracted_word)} - {numeral_number}\n")
