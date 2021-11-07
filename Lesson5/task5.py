# Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

# Генерация
import random

with open("task5.txt", "w") as task5_txt:
    task5_txt.write(' '.join([str(random.randint(1, 101)) for x in range(1, 11)]))

total = 0
task5_input = open("task5.txt")
for element in task5_input.readline().split():
    total += int(element)
task5_input.close()

print(f"Сумма чисел в файле: {total}")
