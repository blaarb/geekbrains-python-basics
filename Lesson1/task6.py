a = int(input("Введите кол-во километров, которое спорсмен пробежал в первый день:\n"))
b = int(input("Введите значение км, которое требуется достигнуть\n"))
i = 1

while a < b:
    a = a + a * 0.1
    i += 1
    # print(a, i)

print("Ответ: на {1}-й день спортсмен достиг результата — не менее {0} км.".format(b, i))