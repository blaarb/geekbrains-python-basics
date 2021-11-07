# Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.

# Генератор
# import names
# import random
# with open("task3.txt", "w") as employees_salaries:
#     for i in range(random.randint(5, 15)):
#         print(names.get_full_name())
#         employees_salaries.write(f"{names.get_full_name()} {random.randint(10, 50) * 1000}\n")

low_salaries = []
salaries = []

with open("task3.txt") as employees_salaries:
    for line in employees_salaries:
        array = line.split()
        salaries.append(int(array[2]))
        if int(array[2]) < 20000:
            low_salaries.append(array[1])

average = sum(salaries) / len(salaries)
print(f"Сотрудники с окладом менее 20 тыс.: {low_salaries}")
print(f"Средняя величина дохода сотрудников: {average}")
