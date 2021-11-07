# Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных,
# практических и лабораторных занятий по этому предмету и их количество.
# Важно, чтобы для каждого предмета не обязательно были все типы занятий.
# Сформировать словарь, содержащий название предмета и общее количество занятий по нему.
# Вывести словарь на экран.


def remove_lesson_types(input_string):
    return int(input_string[:input_string.find('(')])


subjects = {}
with open("task6.txt", encoding='UTF-8') as task6_txt:
    for line in task6_txt:
        line_elements = line.split()
        # print(line_elements)
        subject = line_elements[0]
        subject_total = 0
        for i in range(1, 4):
            if line_elements[i] != '—':
                subject_total += remove_lesson_types(line_elements[i])
        subjects.update({subject: subject_total})

print(subjects)
