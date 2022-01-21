import models
import datetime
import random
import receipts
import Admins_data
import text_information_variables


def fill_out_a_receipt(type_of_technic):
    while True:
        if type_of_technic == "Телефон":
            equipment = models.Phone(input("Модель телефона - "), input("Операционная система - "),
                                     input("Информация о поломке  - "))
            break
        elif type_of_technic == "Ноутбук":
            try:
                equipment = models.Laptop(input("Модель ноутбука - "), input("Операционная система - "),
                                          int(input("Год выпуска - ")), input("Информация о поломке - "))
            except ValueError:
                print(text_information_variables.error_text)
            else:
                break
        elif type_of_technic == "Телевизор":
            try:
                equipment = models.TV(input("Модель телевизора - "), int(input("Диагональ - ")),
                                      input("Информация о поломке  - "))
            except ValueError:
                print(text_information_variables.error_text)
            else:
                break
        else:
            print(text_information_variables.error_text)
            type_of_technic = input("Тип техники - ")
    print("\nВведите персональные данные")
    user_data = models.Receipt(input("Имя - "), input("Очество - "),
                               input("Фамилия - "), equipment, random.randint(1, 1000),
                               datetime.date.today(),
                               datetime.date.today() + datetime.timedelta(random.choice(range(1, 5))),
                               "Техника сдана в ремонт")
    personal_data = f"{user_data.surname} {user_data.name} {user_data.father_name}"
    receipts.dict_with_receipts[user_data.number_of_receipt] = user_data
    if personal_data in receipts.dict_with_receipts:
        receipts.dict_with_receipts[personal_data].append(user_data)
    else:
        receipts.dict_with_receipts[personal_data] = user_data
    return user_data


def search_receipt(user_choice):
    while True:
        if user_choice == "0":
            break
        else:
            receipts.give_out_information(user_choice)
            break


def accept_a_choice(user_choice):
    if user_choice == "Сдаю в ремонт":
        print("Пожалуйста, введите тип техники, сдаваемой в ремонт: ")
        current_technic = input("Тип техники - ")
        print(fill_out_a_receipt(current_technic))
    elif user_choice == "Информация":
        print(text_information_variables.welcome_information_console_text)
        current_user_choice = input("Ф.И.О/Номер квитанции - ")
        search_receipt(current_user_choice)
    elif user_choice == "0":
        print("Мы будем рады видеть Вас в нашем сервисе!")
        exit()
    elif user_choice == "Админ":
        current_login = input("Логин - ")
        current_password = input("Пароль - ")
        Admins_data.log_in_admin(current_login, current_password)
    else:
        print(text_information_variables.error_text)
        user_choice = input("Ввод данных(Сдаю в ремонт/Информация/Админ/0) - ")
        accept_a_choice(user_choice)


def main():
    print(text_information_variables.welcome_text)
    current_choice = input("Ввод данных(Сдаю в ремонт/Информация/Админ/0) - ")
    accept_a_choice(current_choice)


if __name__ == "__main__":
    while True:
        main()
