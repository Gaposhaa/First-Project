import main
import moduls
import datetime
import random
import receipts


def getting_choice(user_choice):
    if user_choice == "Сдаю в ремонт":
        print("""Приветствуем Вас в нашем сервисе по ремонту техники!
Пожалуйста, введите следующие данные:
                    - "Имя"
                    - "Очество"
                    - "Фамилия"
                    - "Тип техники(Телефон, Телевизор, Ноутбук)""")
        user_data = main.Receipt(input("Имя - "), input("Очество - "),
                                 input("Фамилия - "), input("Тип - "), random.randint(1, 1000), datetime.date.today(),
                                 datetime.date.today() + datetime.timedelta(random.choice(range(1, 5))),
                                 "Техника сдана в ремонт")
        while True:
            if user_data.equipment == "Телефон":
                user_data.equipment = moduls.Phone(input("Модель телефона - "), input("Операционная система - "),
                                                   input("Информация о поломке  - "))
                print(user_data)
                break
            elif user_data.equipment == "Ноутбук":
                try:
                    user_data.equipment = moduls.Laptop(input("Модель ноутбука - "),
                                                        input("Операционная система - "),
                                                        int(input("Год выпуска - ")),
                                                        input("Информация о поломке - "))
                except ValueError:
                    print("""Введены не корректные данные в графе "Год выпуска"! """)
                else:
                    print(user_data)
                    break
            elif user_data.equipment == "Телевизор":
                try:
                    user_data.equipment = moduls.TV(input("Модель телевизора - "), int(input("Диагональ - ")),
                                                    input("Информация о поломке  - "))
                except ValueError:
                    print("""Введены не корректные данные в графе "Диагональ"! """)
                else:
                    print(user_data)
                    break
            else:
                print(f"""К сожалению {user_data.name} {user_data.father_name}, мы не обслуживаем данный вид техники,      
либо вы ввели не корректные данные.""")
                user_data.equipment = input()
    elif user_choice == "Информация":
        while True:
            print(f"""Введите Ф.И.О, если хотите получить информацию о всех обращения в наш сервис, 
либо номер квитанции, если хотите получить информацию о конкретном обращении.
Если хотите выйти из приложения, введите 0""")
            current_user_choice = input("Ф.И.О/Номер квитанции - ")
            if current_user_choice == "0":
                print("Мы всегда будем рады видеть Вас в нашем сервисе!")
                break
            else:
                receipts.give_out_information(current_user_choice)
    else:
        print("""Введены не корректные данные в графе "Ваша выбор"! """)
        user_choice = input("Ввод данных(Сдаю в ремонт/Информация) - ")
        getting_choice(user_choice)


if __name__ == "__main__":
    while True:
        print("""Рады приветствовать Вас в нашем сервисе по ремонту техники!
Уважаемый пользователь, выберите действие:
"Сдаю в ремонт"(ввод данных о технике и описание поломки),
"Информация"(Информация о обращениях в наш сервис) """)
        current_choice = input("Ввод данных(Сдаю в ремонт/Информация) - ")
        getting_choice(current_choice)
