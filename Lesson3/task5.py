# Программа запрашивает у пользователя строку чисел, разделенных пробелом.
# При нажатии Enter должна выводиться сумма чисел. Пользователь может продолжить ввод чисел,
# разделенных пробелом и снова нажатьEnter. Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
# Но если вместо числа вводится специальный символ, выполнение программы завершается.
# Если специальный символ введен после нескольких чисел,
# то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.

def sum_list(list):
    sum = 0
    for substring in list:
        if substring != '+':
            sum += int(substring)
        else:
            break
    return sum


input_string = ''
result_sum = 0
while input_string.count('+') == 0:
    input_string = input("Введите строку чисел, разделенных пробелом. "
                         "Чтобы заверить работу программы добавьте в строку символ + через пробел.\n")
    # input_string = "0 10 4 5 1 +"
    result_sum = result_sum + sum_list(input_string.split())
    print(f"Сумма всех введенных чисел: {result_sum}")