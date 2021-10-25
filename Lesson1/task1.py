str = input('Введите строку\n')
print("Ваша строка: %s" % str)
print("В Вашей строке {} слов".format(len(str.split())))

number = float(input('Введите число\n'))
print("Если разделить число {0} на два нацело, то получится {1}).".format(number, number // 2))