import random
import datetime
from abc import ABC, abstractmethod


def execution_of_works(status):
    return status


class Receipt:
    def __init__(self, name, father_name, surname, equipment):
        self.name = name
        self.father_name = father_name
        self.surname = surname
        self.equipment = equipment


print("""Приветствуем Вас в нашем сервисе по ремонту техники!
Пожалуйста, введите следующие данные:
            - "Имя"
            - "Очество"
            - "Фамилия"
            - "Тип техники(Телефон, Телевизор, Ноутбук)""")
user_data = Receipt(input("Имя - "), input("Очество - "), input("Фамилия - "), input("Тип техники - "))
date_of_receipt = datetime.date.today()
numbers_days = 1, 2, 3, 4, 5
deadline = date_of_receipt + datetime.timedelta(random.choice(numbers_days))
full_description = f"""№ квитанции: "{random.randint(1, 1000)}"
Ф.И.О. клиента: "{user_data.surname} {user_data.name} {user_data.father_name}"
Дата принятия в ремонт: {date_of_receipt}
Дата выдачи после ремонта: {deadline}
принят в ремонт: "{user_data.equipment}"
Статус: "{execution_of_works("Техника принята в ремонт")}"
техническая информация/информация о поломке:"""


class Technic(ABC):
    @abstractmethod
    def enter_data(self):
        pass


class Phone(Technic):
    def enter_data(self):
        model = input("Модель - ")
        operation_system = input("Оперционная система - ")
        type_of_breakdown = input("Тип поломки - ")
        print(f"{full_description}, [{model=}, {operation_system=}, {type_of_breakdown=}]")
        return model, operation_system, type_of_breakdown


class TV(Technic):
    def enter_data(self):
        model = input("Модель - ")
        try:
            diagonal = int(input("Диагональ экрана - "))
        except ValueError:
            print("Ведена неверная информация в графе <Диагональ экрана>. Пожалуйста, исправьте данные.")
        else:
            type_of_breakdown = input("Тип поломки - ")
            print(f"{full_description}, [{model=}, {diagonal=}, {type_of_breakdown=}]")
            return model, diagonal, type_of_breakdown


class Laptop(Technic):
    def enter_data(self):
        model = input("Модель - ")
        operation_system = input("Операционная система - ")
        try:
            year_of_release = int(input("Год выпуска - "))
        except ValueError:
            print("Ведена неверная информация в графе <Год выпуска>. Пожалуйста, исправьте данные.")
        else:
            type_of_breakdown = input("Тип поломки - ")
            print(f"{full_description}, [{model=}, {year_of_release=}, {type_of_breakdown=}]")
            return model, year_of_release, operation_system, type_of_breakdown


def output_data(type_of_technic):
    if user_data.equipment == "Телефон":
        type_of_technic = Phone()
        full_description, type_of_technic.enter_data()
    elif user_data.equipment == "Телевизор":
        type_of_technic = TV()
        type_of_technic.enter_data()
    elif user_data.equipment == "Ноутбук":
        type_of_technic = Laptop()
        full_description, type_of_technic.enter_data()
    else:
        print(f"""К сожалению, {user_data.name} {user_data.father_name}, мы не обслуживаем данный вид техники,      
либо вы ввели не корректные данные.
Выберите из доступных видов:
1 - "Телефон"
2 - "Телевизор"
3 - "Ноутбук" """)
        user_data.equipment = input("Тип техники(Телефон, Телевизор, Ноутбук) = ")
        output_data(user_data.equipment)

    return type_of_technic


output_data(user_data.equipment)
