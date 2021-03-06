# Реализовать формирование списка, используя функцию range() и возможности генератора.
# В список должны войти четные числа от 100 до 1000 (включая границы).
# Необходимо получить результат вычисления произведения всех элементов списка.

import functools

generated_list = [x for x in range(1001) if x >= 100 and x % 2 == 0]
# print(generated_list)


def multiply(a, b):
    return a * b


print(functools.reduce(multiply, generated_list))
