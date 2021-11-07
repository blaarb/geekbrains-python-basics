# Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.

incoming_message = 'start'

while incoming_message != '':
    incoming_message = input("Введите новое сообщение, или нажмите Enter, чтобы завершить ввода\n")
    with open("task1_file.txt", "a") as file_to_write_into:
        file_to_write_into.write(f"{incoming_message}\n")
