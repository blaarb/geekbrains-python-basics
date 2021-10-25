n = int(input('Введите положительное целое число n\n'))
result = 0

while n // 10 != 0:
    if result < n % 10:
        result = n % 10
    n = n // 10
else:
    if result < n:
        result = n

print("Самая большая цифра:" + str(result))