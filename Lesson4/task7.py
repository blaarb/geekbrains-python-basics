# Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение.
# При вызове функции должен создаваться объект-генератор.
# Функция должна вызываться следующим образом: for el in fact(n).
# Функция отвечает за получение факториала числа,
# а в цикле необходимо выводить только первые n чисел, начиная с 1! и до n!.

import math

n = int(input("Введите n:\n"))


def fact(n):
    for i in range(n):
        yield math.factorial(i + 1)


for element in fact(n):
    print(element)
