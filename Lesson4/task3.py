# Для чисел в пределах от 20 до 240 найти числа, кратные 20 или 21. Необходимо решить задание в одну строку.

print([x for x in range(240) if (x % 20 == 0 or x % 21 == 0) and x >= 20 ])
