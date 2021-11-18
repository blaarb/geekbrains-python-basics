from abc import ABC, abstractmethod

class Warehouse:

    departments = {
        "front office": [],
        "back office": [],
        "accounting": [],
        "HR": []
    }

    @classmethod
    def add_unit(cls, input_object, dept_key):
        mutable = cls.departments.get(dept_key)
        mutable.append(input_object)
        cls.departments.update({dept_key: mutable})


class OrgTechUnit():
    name = ''
    paper_formats = ["A4", "A3", "B5", "b4"]
    voltage = 220
    display_type = "LED"
    has_ethernet = True
    black_cartridge_model = ""
    colour_cartridge_model = ""
    has_wifi = False
    department = ''

    def update_dept(self, dept_key):
        Warehouse.add_unit(self, dept_key)
        self.department = dept_key


class Printer(OrgTechUnit):
    manufacturers = ["HP", "Cannon", 'Brother']
    print_tech = "struini"
    max_resolution = "5760х1440"

    def __init__(self):
        super().__init__()
        print(f"На склад был добавлен принтер.")


class Scanner(OrgTechUnit):
    scan_speed = (15, 10)
    resolution = "600x600"
    manufacturers = ["HP", "Cannon", 'Brother', 'Epson']


class Xerox(OrgTechUnit):
    max_copy_per_cycle = [99, 60, 50, 10]


printer01 = Printer()
printer01.update_dept("HR")
print(Warehouse.departments)