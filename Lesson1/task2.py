time = int(input("Введите время в секундах:\n"))

hour = time // 3600
time %= 3600
min = time // 60
time %= 60


print("Время в часах, минутах и секундах: %02d:%02d:%02d" % (hour, min, time))