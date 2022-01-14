class Technic:
    def __init__(self, model, type_of_breakdown):
        self.model = model
        self.type_of_breakdown = type_of_breakdown

    def fill_in_receipt(self):
        return f"""Модель: {self.model}
Информация о неисправности: {self.type_of_breakdown}"""


class Phone(Technic):
    def __init__(self, model, operation_system, type_of_breakdown):
        super().__init__(model, type_of_breakdown)
        self.operation_system = operation_system

    def __str__(self):
        return f"""Техническая информация: Операционная система - {self.operation_system}"""


class TV(Technic):
    def __init__(self, model, diagonal, type_of_breakdown):
        super().__init__(model, type_of_breakdown)
        self.diagonal = diagonal

    def __str__(self):
        return f"""Техническая информация: Диагональ - {self.diagonal} """


class Laptop(Technic):
    def __init__(self, model, operation_system, year_of_release, type_of_breakdown):
        super().__init__(model, type_of_breakdown)
        self.operation_system = operation_system
        self.year_of_release = year_of_release

    def __str__(self):
        return f"""Техническая информация: Операционная система - {self.operation_system},
                                          Год выпуска - {self.year_of_release} """
