from itertools import count, cycle
from random import randint


def guess():
    return int(input("Чему равен его квадрат\n"))


print("итератор, генерирующий целые числа, начиная с указанного.\n")

list1 = []
limit = randint(5, 10)
for i in count(3):
    print(i)
    list1.append(i)
    if i == limit:
        break
print(list1)

print("итератор, повторяющий элементы некоторого списка, определенного заранее.\n")

list2 = [randint(1, 10) for x in range(10)]
print(list2)
for element in cycle(list2):
    print(f"Текущее число: {element}")
    guess_number = guess()
    print(guess_number)
    if guess_number == element ** 2:
        break
