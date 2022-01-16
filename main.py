class Receipt:
    def __init__(self, name, father_name, surname, equipment, number_of_receipt, date_of_receipt, deadline, status):
        self.name = name
        self.father_name = father_name
        self.surname = surname
        self.equipment = equipment
        self.number_of_receipt = number_of_receipt
        self.date_of_receipt = date_of_receipt
        self.deadline = deadline
        self.status = status

    def __str__(self):
        return f"""№ квитанции: "{self.number_of_receipt }"
Ф.И.О. : {self.surname} {self.name} {self.father_name}
Тип техники сдаваемой в ремонт: {self.equipment}
Дата приема: {self.date_of_receipt}
Дата выдачи: {self.deadline}
Статус: {self.status}"""
