import random
from abc import ABC, abstractmethod


class Receipt:
    def __init__(self, name, father_name, surname, equipment):
        self.name = name
        self.father_name = father_name
        self.surname = surname
        self.equipment = equipment


class Technic(ABC):
    @abstractmethod
    def enter_data(self):
        pass


class Phone(Technic):
    def enter_data(self):
        model = input("Модель = ")
        operation_system = input("Оперционная система = ")
        type_of_breakdown  = input("Тип поломки = ")
        return model, operation_system, type_of_breakdown


class TV(Technic):
    def enter_data(self):
        model = input("Модель = ")
        diagonal = input("Диагональ экрана = ")
        type_of_breakdown  = input("Тип поломки = ")
        return model, diagonal, type_of_breakdown


class Laptop(Technic):
    def enter_data(self):
        model = input("Модель = ")
        operation_system = input("Операционная система = ")
        year = input("Год выпуска = ")
        type_of_breakdown = input("Тип поломки = ")
        return model, year, operation_system, type_of_breakdown


print("""Приветствуем Вас в нашем сервисе по ремонту техники!
Пожалуйста, введите следующие данные:""")

user_date = Receipt(input("Имя - "), input("Очество - "), input("Фамилия - "),
input("Тип техники(Телефон, Телевизор, Ноутбук) - "))


def output_data(type_of_technic):
    full_description = (f"""№ квитанции: "{random.randint(1, 1000)}"
Ф.И.О. клиента: "{user_date.surname} {user_date.name} {user_date.father_name}"
принят в ремонт: "{user_date.equipment}" 
техническая информация/информация о поломке:""")
    if user_date.equipment == "Телефон":
        type_of_technic = Phone()
        print(full_description, type_of_technic.enter_data())
    elif user_date.equipment == "Телевизор":
        type_of_technic = TV()
        print(full_description, type_of_technic.enter_data())
    elif user_date.equipment == "Ноутбук":
        type_of_technic = Laptop()
        print(full_description, type_of_technic.enter_data())
    else:
        print(f"""К сожалению, {user_date.name} {user_date.father_name}, мы не обслуживаем данный вид техники,      
либо вы ввели не корректные данные.
Выберите из доступных видов:
1 - "Телефон"
2 - "Телевизор"
3 - "Ноутбук" """)
        user_date.equipment = input("Тип техники(Телефон, Телевизор, Ноутбук) = ")
        output_data(user_date.equipment)
    return user_date.equipment


output_data(user_date.equipment)
deadlines = "один день", "два дня", "три дня", "четыре дня", "пять дней"
print(f"""Уважаемый(ая) {user_date.name} {user_date.father_name}, ваш заказ будет готов через
{random.choice(deadlines)} со дня поступленя заявки.""")



