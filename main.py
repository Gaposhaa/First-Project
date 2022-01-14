class Receipt:
    def __init__(self, name, father_name, surname, equipment, number_of_receipt):
        self.name = name
        self.father_name = father_name
        self.surname = surname
        self.equipment = equipment
        self.number_of_receipt = number_of_receipt

    def fill_user_data(self):
        return f"""№ квитанции: "{self.number_of_receipt }"
Ф.И.О. : {self.surname} {self.name} {self.father_name}
Тип техники сдаваемой в ремонт: {self.equipment}"""


class Dates:
    def __init__(self, date_of_receipt, deadline):
        self.date_of_receipt = date_of_receipt
        self.deadline = deadline

    def __str__(self):
        return f"""Дата сдачи техники в ремонт: {self.date_of_receipt}
Дата выдачи техники после ремонта: {self.deadline}"""


class Status:
    def __init__(self, status):
        self.status = status

    def __str__(self):
        return f"""Статус: {self.status}"""
