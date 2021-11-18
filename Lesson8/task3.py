class ListWrongElementType(Exception):

    def __init__(self, error_message):
        self.error_message = error_message


def check_if_num(input_string):
    if input_string == "stop":
        return True
    stripped_string = input_string.lstrip("-")
    i = 0
    while i <= len(stripped_string) - 1:
        if stripped_string[i] not in ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9"):
            return False
        i += 1
    return True


last_input = ''
result_list = []
while last_input != "stop":
    last_input = input("Введите очередное число или слово stop, чтобы остановиться\n")
    keep = True
    try:
        if check_if_num(last_input):
            result_list.append(last_input)
        else:
            raise ListWrongElementType("Это не число!")
    except ListWrongElementType as e:
        print(e)

result_list.remove("stop")
print([int(x) for x in result_list])