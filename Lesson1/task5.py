import math

income = float(input("Укажите размер выручки фирмы\n"))
expenses = float(input("Укажите размер издержек\n"))

profitability = income / expenses

if income > expenses:
    print("Фирма работает с прибылью. Ее рентабельность составляет {}".format(profitability))
    number_of_employees = float(input("Введите количество сотрудников в штате:\n"))
    print("Прибыль фирмы в расчете на одного сотрудника составляет {}".format(income / number_of_employees))
elif income < expenses:
    print("Фирма работает с убытками")