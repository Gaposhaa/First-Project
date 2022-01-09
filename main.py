import random
import datetime
from abc import ABC, abstractmethod


class Receipt:
    def __init__(self, name, father_name, surname, equipment, status):
        self.name = name
        self.father_name = father_name
        self.surname = surname
        self.equipment = equipment
        self.status = status

    def func(self):
        return f"""№ квитанции: "{random.randint(1, 1000)}"
    Ф.И.О. клиента: "{self.surname}  {self.name} {self.father_name}"
    Дата принятия в ремонт: {date_of_receipt}
    Дата выдачи после ремонта: {deadline}
    Статус: {self.status}
    Техническая информация/информация о поломке: {self.equipment} - """

    def getting_technic_information(self, user_data):
        if self.equipment == "Телефон":
            current_phone = Phone()
            current_phone.receiving_data(user_data)
        elif self.equipment == "Телевизор":
            current_tv = TV()
            current_tv.receiving_data(user_data)
        elif self.equipment == "Ноутбук":
            current_laptop = Laptop()
            current_laptop.receiving_data(user_data)
        else:
            print(f"""К сожалению {self.name} {self.father_name}, мы не обслуживаем данный вид техники,      
            либо вы ввели не корректные данные.
            Выберите из доступных видов:
            1 - "Телефон"
            2 - "Телевизор"
            3 - "Ноутбук" """)
            self.equipment = input("Тип техники(Телефон, Телевизор, Ноутбук) = ")
            user_data.getting_technic_information(user_data)


class Technic(ABC):
    @abstractmethod
    def receiving_data(self, user_data):
        pass


class Phone(Technic):
    def receiving_data(self, user_data):
        model = input("Модель - ")
        operation_system = input("Операционная система - ")
        type_of_breakdown = input("Тип поломки - ")
        print(f"{Receipt.func(user_data)}{model=},{operation_system=},{type_of_breakdown=}")


class TV(Technic):
    def receiving_data(self, user_data):
        while True:
            model = input("Модель - ")
            try:
                diagonal = int(input("Диагональ экрана - "))
            except ValueError:
                print("Введена не корректная информация. Пожалуйста, исправьте.")
            else:
                type_of_breakdown = input("Тип поломки - ")
                print(f"{Receipt.func(user_data)}{model=}, {diagonal=}, {type_of_breakdown=}")
                break


class Laptop(Technic):
    def receiving_data(self, user_data):
        while True:
            model = input("Модель - ")
            operation_system = input("Операционная система - ")
            try:
                year_of_release = int(input("Год выпуска - "))
            except ValueError:
                print("Введена не корректная информация. Пожалуйста, исправьте.")
            else:
                type_of_breakdown = input("Тип поломки - ")
                print(f"""{Receipt.func(user_data)}
{model=}, {year_of_release=}, {operation_system=}, {type_of_breakdown=}""")
                break


date_of_receipt = datetime.date.today()
deadline = date_of_receipt + datetime.timedelta(random.choice(range(1, 5)))


if __name__ == "__main__":
    print("""Приветствуем Вас в нашем сервисе по ремонту техники!
    Пожалуйста, введите следующие данные:
                - "Имя"
                - "Очество"
                - "Фамилия"
                - "Тип техники(Телефон, Телевизор, Ноутбук)""")

    user_data = Receipt(input("Имя - "), input("Очество - "), input("Фамилия - "), input("Тип - "), "Сдана в ремонт")
    date_of_receipt = datetime.date.today()
    deadline = date_of_receipt + datetime.timedelta(random.choice(range(1, 5)))
    user_data.getting_technic_information(user_data)
