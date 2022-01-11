import random
import datetime
from abc import ABC, abstractmethod


class Receipt:
    def __init__(self, name, father_name, surname, equipment):
        self.name = name
        self.father_name = father_name
        self.surname = surname
        self.equipment = equipment

    def filling_out_a_receipt(self):
        if self.equipment == "Телефон":
            current_phone = Phone(input("Модель - "), input("Операционная система - "), input("Тип поломки - "),
                                  datetime.date.today(),
                                  datetime.date.today() + datetime.timedelta(random.choice(range(1, 5))), "В ремонте",
                                  random.randint(1, 1000))
            print(f"""№ квитанции: "{current_phone.number_of_receipt}"
Ф.И.О. клиента: "{self.surname}  {self.name} {self.father_name}"
Дата принятия в ремонт: {current_phone.date_of_receipt}
Дата выдачи после ремонта: {current_phone.deadline}
Статус: {current_phone.status}
Техническая информация/информация о поломке: {self.equipment} -
{current_phone.model = }, {current_phone.operation_system = }, {current_phone.type_of_breakdown = }""")
        elif self.equipment == "Телевизор":
            try:
                current_tv = TV(input("Модель - "), int(input("Диагональ - ")), input("Неисправность - "),
                                datetime.date.today(),
                                datetime.date.today() + datetime.timedelta(random.choice(range(1, 5))), "В ремонте",
                                random.randint(1, 1000))
            except ValueError:
                print("Введена не корректная информация. Пожалуйста, исправьте.")
                user_data.filling_out_a_receipt()
            else:
                print(f"""№ квитанции: "{current_tv.number_of_receipt}"
Ф.И.О. клиента: "{self.surname}  {self.name} {self.father_name}"
Дата принятия в ремонт: {current_tv.date_of_receipt}
Дата выдачи после ремонта: {current_tv.deadline}
Статус: {current_tv.status}
Техническая информация/информация о поломке: {self.equipment} -
{current_tv.model = }, {current_tv.diagonal = }, {current_tv.type_of_breakdown = }""")
        elif self.equipment == "Ноутбук":
            try:
                current_laptop = Laptop(input("Модель - "), input("OS - "), int(input("Год - ")),
                                        input("Неисправность - "),
                                        datetime.date.today(),
                                        datetime.date.today() + datetime.timedelta(random.choice(range(1, 5))),
                                        "В ремонте", random.randint(1, 1000))
            except ValueError:
                print("Введена не корректная информация. Пожалуйста, исправьте.")
                user_data.filling_out_a_receipt()
            else:
                print(f"""№ квитанции: "{current_laptop.number_of_receipt}"
Ф.И.О. клиента: "{self.surname}  {self.name} {self.father_name}"
Дата принятия в ремонт: {current_laptop.date_of_receipt}
Дата выдачи после ремонта: {current_laptop.deadline}
Статус: {current_laptop.status}
Техническая информация/информация о поломке: {self.equipment} -
{current_laptop.model = }, {current_laptop.operation_system = }, 
{current_laptop.year_of_release = }, {current_laptop.type_of_breakdown = }""")
        else:
            print(f"""К сожалению {self.name} {self.father_name}, мы не обслуживаем данный вид техники,      
либо вы ввели не корректные данные.
Выберите из доступных видов:
1 - "Телефон"
2 - "Телевизор"
3 - "Ноутбук" """)
            self.equipment = input("Тип техники(Телефон, Телевизор, Ноутбук) = ")
            user_data.filling_out_a_receipt()


class NumberOfReceipt:
    def __init__(self, number):
        self.number = number


class Technic(ABC):
    @abstractmethod
    def __init__(self):
        pass


class Phone(Technic):
    def __init__(self, model, operation_system, type_of_breakdown, date_of_receipt, deadline, status,
                 number_of_receipt):
        self.model = model
        self.operation_system = operation_system
        self.type_of_breakdown = type_of_breakdown
        self.date_of_receipt = date_of_receipt
        self.deadline = deadline
        self.status = status
        self.number_of_receipt = number_of_receipt


class TV(Technic):
    def __init__(self, model, diagonal, type_of_breakdown, date_of_receipt, deadline, status, number_of_receipt):
        self.model = model
        self.diagonal = diagonal
        self.type_of_breakdown = type_of_breakdown
        self.date_of_receipt = date_of_receipt
        self.deadline = deadline
        self.status = status
        self.number_of_receipt = number_of_receipt


class Laptop(Technic):
    def __init__(self, model, operation_system, year_of_release, type_of_breakdown, date_of_receipt, deadline, status,
                 number_of_receipt):
        self.model = model
        self.operation_system = operation_system
        self.year_of_release = year_of_release
        self.type_of_breakdown = type_of_breakdown
        self.date_of_receipt = date_of_receipt
        self.deadline = deadline
        self.status = status
        self.number_of_receipt = number_of_receipt


if __name__ == "__main__":
    print("""Приветствуем Вас в нашем сервисе по ремонту техники!
Пожалуйста, введите следующие данные:
            - "Имя"
            - "Очество"
            - "Фамилия"
            - "Тип техники(Телефон, Телевизор, Ноутбук)""")

    user_data = Receipt(input("Имя - "), input("Очество - "), input("Фамилия - "), input("Тип - "))
    user_data.filling_out_a_receipt()
