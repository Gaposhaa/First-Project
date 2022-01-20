class Technic:
    def __init__(self, model, type_of_breakdown):
        self.model = model
        self.type_of_breakdown = type_of_breakdown

    def __str__(self):
        return f"""Модель: {self.model}
Информация о неисправности: {self.type_of_breakdown}"""


class Phone(Technic):
    def __init__(self, model, operation_system, type_of_breakdown):
        super().__init__(model, type_of_breakdown)
        self.operation_system = operation_system

    def __str__(self):
        return f"""Телефон
{super().__str__()}
Техническая информация: Операционная система - {self.operation_system}"""


class TV(Technic):
    def __init__(self, model, diagonal, type_of_breakdown):
        super().__init__(model, type_of_breakdown)
        self.diagonal = diagonal

    def __str__(self):
        return f"""Телевизор
{super().__str__()}
Техническая информация: Диагональ - {self.diagonal}"""


class Laptop(Technic):
    def __init__(self, model, operation_system, year_of_release, type_of_breakdown):
        super().__init__(model, type_of_breakdown)
        self.operation_system = operation_system
        self.year_of_release = year_of_release

    def __str__(self):
        return f"""Ноутбук
{super().__str__()}
Техническая информация: Операционная система - {self.operation_system}; Год выпуска - {self.year_of_release} """


class Receipt:
    def __init__(self, surname, name, father_name, equipment, number_of_receipt, date_of_receipt, deadline, status):
        self.surname = surname
        self.name = name
        self.father_name = father_name
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

