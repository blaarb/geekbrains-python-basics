# Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
# В расчете необходимо использовать формулу:
# (выработка в часах * ставка в час) + премия.
# Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.

import argparse

parser = argparse.ArgumentParser(description='Программа для вычисления зарплаты.')
parser.add_argument('hours', help="Сколько часов отработал сотрудник", type=float)
parser.add_argument('wage', help="Ставка", type=float)
parser.add_argument('-b', '--bonus', help="Премия. Если пропустить этот аргумент, то он будет равен 0", default=0, type=float)

args = parser.parse_args()

print(f"Звработная плата составляет {args.hours * args.wage + args.bonus} рублей.")
