# Для списка реализовать обмен значений соседних элементов, т.е. Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().

list = [ "Пользователь", 1, True, "ввел", "число", 3.5, "Результат:", (42, 24)]
print(list)
result_list = []

for i in range(len(list)):
    if i % 2 != 0:
        result_list.insert(i - 1, list[i])
    elif i % 2 == 0:
        result_list.insert(i + 1, list[i])

print(result_list)