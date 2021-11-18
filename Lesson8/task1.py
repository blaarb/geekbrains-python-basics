class FormattedDate:
    day = 0
    month = 0
    year = 0

    def __init__(self, input_string):
        FormattedDate.convert_to_int(input_string)

    @classmethod
    def convert_to_int(cls, input_string):
        list_of_strings = input_string.split('-')
        cls.day = int(list_of_strings[0])
        cls.month = int(list_of_strings[1])
        cls.year = int(list_of_strings[2])
        FormattedDate.validate_ints(cls.day, cls.month, cls.year)

    @staticmethod
    def validate_ints(day, month, year):
        days_months = {
            "01": (range(1, 32)),
            "02": (range(1, 29)),
            "03": (range(1, 32)),
            "04": (range(1, 31)),
            "05": (range(1, 32)),
            "06": (range(1, 31)),
            "07": (range(1, 32)),
            "08": (range(1, 32)),
            "09": (range(1, 31)),
            "10": (range(1, 32)),
            "11": (range(1, 31)),
            "12": (range(1, 32)),
        }

        if year not in (range(1990, 2051)):
            return "День месяца указан неправильно"
        elif month not in range(1, 13):
            return "Месяц указан неправильно"
        elif day not in days_months[str(month)]:
            return "Год указан неправильно"
        print(f"день = {day}, месяц = {month}, год = {year}")


today = FormattedDate("17-11-2021")
