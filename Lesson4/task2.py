# Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.

import random

list1 = [random.randint(1, 1000) for x in range(20)]
print(list1)

print([element for element in list1[1:] if element > list1[list1.index(element) - 1]])
