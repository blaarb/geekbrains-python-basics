class Worker:
    name = ""
    surname = ""
    position = "Senior Data Scientist"
    _income = {"wage": 42000, "bonus": 0}


_income["wage"]

class Position(Worker):
    def get_full_name(self):
        return f"Полное имя сотрудника: {self.name} {self.surname}"

    def get_total_income(self):
        return f"Его доход с учетом бонусов: {self._income.get('wage') + self._income.get('bonus')}"


employee01 = Position()

employee01.name = "Tair"
employee01.surname = "Yunussov"

print(employee01.get_full_name())

employee01._income = {"wage": 600000, "bonus": 200000}

print(employee01.get_total_income())
