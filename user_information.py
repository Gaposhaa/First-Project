import main
import moduls
import datetime
import random
import receipts


class Information:

    def __init__(self, user_choice):
        self.user_choice = user_choice

    def getting_choice(self):
        if self.user_choice == "Сдаю в ремонт":
            print("""Приветствуем Вас в нашем сервисе по ремонту техники!
Пожалуйста, введите следующие данные:
                            - "Имя"
                            - "Очество"
                            - "Фамилия"
                            - "Тип техники(Телефон, Телевизор, Ноутбук)""")
            user_data = main.Receipt(input("Имя - "), input("Очество - "),
                                     input("Фамилия - "), input("Тип - "), random.randint(1, 1000))
            current_date = main.Dates(datetime.date.today(),
                                      datetime.date.today() + datetime.timedelta(random.choice(range(1, 5))))
            current_status = main.Status("Техника сдана в ремонт")
            if user_data.equipment == "Телефон":
                current_phone_data = moduls.Phone(input("Модель телефона - "), input("Операционная система - "),
                                                  input("Информация о поломке  - "))
                print(f"""{user_data.fill_user_data()}
                {current_phone_data.fill_in_receipt()}
                {current_phone_data.__str__()}
                {current_date.__str__()}
                {current_status.__str__()}""")
            elif user_data.equipment == "Ноутбук":
                while True:
                    try:
                        current_laptop_data = moduls.Laptop(input("Модель ноутбука - "),
                                                            input("Операционная система - "),
                                                            int(input("Год выпуска - ")),
                                                            input("Информация о поломке - "))
                    except ValueError:
                        print("""Введены не корректные данные в графе "Год выпуска"! """)
                    else:
                        print(f"""
                        {user_data.fill_user_data()}
                        {current_laptop_data.fill_in_receipt()}
                        {current_laptop_data.__str__()}
                        {current_date.__str__()}
                        {current_status.__str__()}""")
                        break
            elif user_data.equipment == "Телевизор":
                while True:
                    try:
                        current_tv_data = moduls.TV(input("Модель телефона - "), int(input("Диагональ - ")),
                                                    input("Информация о поломке  - "))
                    except ValueError:
                        print("""Введены не корректные данные в графе "Диагональ"! """)
                    else:
                        print(f"""
                        {user_data.fill_user_data()}
                        {current_tv_data.fill_in_receipt()}
                        {current_tv_data.__str__()}
                        {current_date.__str__()}
                        {current_status.__str__()}""")
                        break
            else:
                print(f"""К сожалению {user_data.name} {user_data.father_name}, мы не обслуживаем данный вид техники,      
                либо вы ввели не корректные данные.
                Выберите из доступных видов:
                1 - "Телефон"
                2 - "Телевизор"
                3 - "Ноутбук" """)
                user_data.equipment = input("Тип техники(Телефон, Телевизор, Ноутбук) = ")
                current_choice.getting_choice()
        elif self.user_choice == "Информация":
            print(f"""Введите Ф.И.О, если хотите получить информацию о всех обращения в наш сервис, либо номер квитанции
если хотите получить информацию о конкретном обращении. Если хотите выйти из приложения, введите 0 """)
            current_user_choice = input("Ф.И.О/Номер квитанции - ")
            if current_user_choice == 0:
                print(f"""Мы всегда будем рады видеть Вас в нашем сервисе!""")
            else:
                receipts.give_out_information(current_user_choice)
        else:
            print("""Введены не корректные данные в графе "Ваша выбор"! """)
            self.user_choice = input("Ввод данных(Сдаю в ремонт/Информация) - ")
            current_choice.getting_choice()


if __name__ == "__main__":
    print("""Уважаемый пользователь, выберите действие. 
"Сдаю в ремонт"(ввод данных о технике и описание поломки),
"Информация"(Информация о обращениях в наш сервис) """)
    current_choice = Information(input("Ввод данных(Сдаю в ремонт/Информация) - "))
    current_choice.getting_choice()
