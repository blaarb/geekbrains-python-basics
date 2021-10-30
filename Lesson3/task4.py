# Программа принимает действительное положительное число x и целое отрицательное число y.
# Необходимо выполнить возведение числа x в степень y. Задание необходимо реализовать в виде функции my_func(x, y).
# При решении задания необходимо обойтись без встроенной функции возведения числа в степень.

def power_of(base, power):
    if power == 1:
        return base
    else:
        return base * power_of(base, power - 1)

def negative_power_of(x, y):
    return 1 / power_of(x, abs(y))

x = float(input("Введите действительное положительное число (основание)\n"))
y = int(input("Введите целое отрицательное число (степень)\n"))

print(negative_power_of(x, y))
