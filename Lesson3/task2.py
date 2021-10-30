# Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.

def print_personal_data(name, last_name, gender, birthyear, cityofr, email, telnumber):
    print("{0} {1} роди{2} в {3} году, проживает в городе {4}, а его контактные данные: {5} и {6}.".format(name, last_name, "лась" if gender == "female" else "лся", birthyear, cityofr, email, telnumber))

print_personal_data(name="Таир", last_name="Юнусов", gender="male", birthyear="1990", cityofr="Алматы", email="tair@gb.ru", telnumber="87776665544")