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


class Technic(ABC):
    @abstractmethod
    def receiving_data(self):
        pass


class Phone(Technic):
    def receiving_data(self):
        model = input("Модель - ")
        operation_system = input("Оперционная система - ")
        type_of_breakdown = input("Тип поломки - ")
        print(f"{full_description} {user_data.equipment} - {model=}, {operation_system=}, {type_of_breakdown=}")


class TV(Technic):
    def receiving_data(self):
        while True:
            model = input("Модель - ")
            try:
                diagonal = int(input("Диагональ экрана - "))
            except ValueError:
                print("Введена не корректная информация. Пожалуйста, исправьте.")
            else:
                type_of_breakdown = input("Тип поломки - ")
                print(f"{full_description} {user_data.equipment} - {model=}, {diagonal=}, {type_of_breakdown=}")
                break


class Laptop(Technic):
    def receiving_data(self):
        while True:
            model = input("Модель - ")
            operation_system = input("Операционная система - ")
            try:
                year_of_release = int(input("Год выпуска - "))
            except ValueError:
                print("Введена не корректная информация. Пожалуйста, исправьте.")
            else:
                type_of_breakdown = input("Тип поломки - ")
                print(f"""{full_description} {user_data.equipment} - {model=}, {year_of_release=}, {operation_system=}
{type_of_breakdown=}""")
                break


def getting_technic_information(type_of_technic):
    if user_data.equipment == "Телефон":
        current_phone = Phone()
        current_phone.receiving_data()
    elif user_data.equipment == "Телевизор":
        current_tv = TV()
        current_tv.receiving_data()
    elif user_data.equipment == "Ноутбук":
        current_laptop = Laptop()
        current_laptop.receiving_data()
    else:
        print(f"""К сожалению, {user_data.name} {user_data.father_name}, мы не обслуживаем данный вид техники,      
либо вы ввели не корректные данные.
Выберите из доступных видов:
1 - "Телефон"
2 - "Телевизор"
3 - "Ноутбук" """)
        user_data.equipment = input("Тип техники(Телефон, Телевизор, Ноутбук) = ")
        getting_technic_information(user_data.equipment)
    return type_of_technic


if __name__ == "__main__":
    print("""Приветствуем Вас в нашем сервисе по ремонту техники!
    Пожалуйста, введите следующие данные:
                - "Имя"
                - "Очество"
                - "Фамилия"
                - "Тип техники(Телефон, Телевизор, Ноутбук)""")

    user_data = Receipt(input("Имя - "), input("Очество - "), input("Фамилия - "), input("Тип техники - "))
    date_of_receipt = datetime.date.today()
    deadline = date_of_receipt + datetime.timedelta(random.choice(range(1, 5)))
    full_description = f"""№ квитанции: "{random.randint(1, 1000)}"
    Ф.И.О. клиента: "{user_data.surname}  {user_data.name} {user_data.father_name}"
    Дата принятия в ремонт: {date_of_receipt}
    Дата выдачи после ремонта: {deadline}
    Статус: "{execution_of_works("Техника принята в ремонт")}"
    Техническая информация/информация о поломке:"""
    getting_technic_information(user_data.equipment)
