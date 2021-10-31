def input_position():
    name = input("Введите название\n")
    price = input("Введите цену\n")
    quantity = input("Введите количество\n")
    units = input("Введите единицы измерения\n")
    return len(input_list) + 1, {"название": name, "цена": price, "количество": quantity, "ed": units}


# input_list = [
#     (1, {"название": "компьютер", "цена": 20000, "количество": 5, "eд": "шт"}),
#     (2, {"название": "принтер", "цена": 6000, "количество": 2, "eд": "шт"}),
#     (3, {"название": "сканер", "цена": 2000, "количество": 7, "eд": "шт"})
# ]

input_list = []
end = False
while not end:
    input_list.append(input_position())
    control_key = input("Введите + для завршения ввода списка или нажмите Enter для продолжения.\n")
    if control_key == "+":
        end = True

print(f"Изначальный список: {input_list}")

nameset = set()
priceset = set()
quantityset = set()
unitset = set()
for tuple_element in input_list:
    # print(tuple_element)
    # print(tuple_element[1].items())
    for item in tuple_element[1].items():
        # print(item)
        if item[0] == "название":
            nameset.add(item[1])
        elif item[0] == "цена":
            priceset.add(item[1])
        elif item[0] == "количество":
            quantityset.add(item[1])
        elif item[0] == "ed":
            unitset.add(item[1])

result_dict = {
    "название": list(nameset),
    "цена": list(priceset),
    "количество": list(quantityset),
    "eд": list(unitset)
}

print(result_dict)
