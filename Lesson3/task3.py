# Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.

def my_func(a, b, c):
    temp_list = [a, b, c]
    min_number = min(temp_list)
    temp_list.remove(min_number)
    return sum(temp_list)

print(my_func(-40, -10, 20))
