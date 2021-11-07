# Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.

ln_num = 0
with open("task2.txt") as file_to_read:
    for line in file_to_read:
        ln_num += 1
        print(f"В строке {ln_num} {len(line.split())} слов.")

print(f"В файле {file_to_read.name} {ln_num} строк")