import user_information
import models
import datetime
import random
import receipts


def fill_out_a_receipt(user_choice):
    if user_choice == "Сдаю в ремонт":
        print("Пожалуйста, введите тип техники, сдаваемой в ремонт: ")
        type_of_technic = input("Тип техники - ")
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
                    print("""Введены не корректные данные в графе "Год выпуска"! """)
                else:
                    break
            elif type_of_technic == "Телевизор":
                try:
                    equipment = models.TV(input("Модель телевизора - "), int(input("Диагональ - ")),
                                          input("Информация о поломке  - "))
                except ValueError:
                    print("""Введены не корректные данные в графе "Диагональ"! """)
                else:
                    break
            else:
                print(f"""К сожалению мы не обслуживаем данный вид техники,      
            либо вы ввели не корректные данные.""")
                type_of_technic = input()
        user_data = user_information.Receipt(input("Имя - "), input("Очество - "),
                                             input("Фамилия - "), equipment, random.randint(1, 1000),
                                             datetime.date.today(),
                                             datetime.date.today() + datetime.timedelta(random.choice(range(1, 5))),
                                             "Техника сдана в ремонт")
        return user_data


def search_receipt(user_choice):
    if user_choice == "Информация":
        while True:
            print("Введите Ф.И.О, если хотите получить информацию о всех обращения в наш сервис, либо номер квитанции,"
                  "если хотите получить информацию о конкретном обращении.\nЕсли хотите вернуться в меню ввода данных, "
                  " введите 0")
            current_user_choice = input("Ф.И.О/Номер квитанции - ")
            if current_user_choice == "0":
                main()
            else:
                receipts.give_out_information(current_user_choice)


def accept_a_choice(user_choice):
    if user_choice == "Сдаю в ремонт":
        print(fill_out_a_receipt(user_choice))
    elif user_choice == "Информация":
        search_receipt(user_choice)
    elif user_choice == "0":
        print("Мы будем рады видеть Вас в нашем сервисе!")
        exit()
    else:
        print("Введены не корректные данные в графе Ваш выбор!")
        user_choice = input("Ввод данных(Сдаю в ремонт/Информация) - ")
        accept_a_choice(user_choice)


def main():
    print("Рады приветствовать Вас в нашем сервисе по ремонту техники!\nУважаемый пользователь, выберите действие:\n"
          "Сдаю в ремонт(ввод данных о технике и описание поломки),\nИнформация(Информация о обращениях в наш сервис)\n"
          "Если хотите выйти из приложения, введите 0")
    current_choice = input("Ввод данных(Сдаю в ремонт/Информация/0) - ")
    accept_a_choice(current_choice)


if __name__ == "__main__":
    main()
