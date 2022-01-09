import main
import receipts


class Information:
    print("""Уважаемый пользователь, выберите действие. "Сдаю в ремонт"(ввод данных о технике и описание поломки),
"Информация"(Информация о обращениях в наш сервис) """)

    def __init__(self, user_choice):
        self.user_choice = user_choice

    def getting_choice(self, current_choice):
        if self.user_choice == "Сдаю в ремонт":
            print("""Приветствуем Вас в нашем сервисе по ремонту техники!
Пожалуйста, введите следующие данные:
                            - "Имя"
                            - "Очество"
                            - "Фамилия"
                            - "Тип техники(Телефон, Телевизор, Ноутбук)""")
            user_choice = main.Receipt(input("Имя - "), input("Очество - "),
                                       input("Фамилия - "), input("Тип - "), "Ремонт")
            user_choice.getting_technic_information(user_choice)
        elif self.user_choice == "Информация":
            print("""Если Вас интересует информация о конкретном обращении в наш сервис,
введите "Да" в графе "Ваш выбор", далее введите номер квитанции.
Если Вы хотите получить данные о всех обращениях в наш сервис, введите "Нет" в графе "Ваш выбор", 
далее введите ФИО, вы получите данную информацию.""")

            our_choice = input("Ваш выбор - ")
            if our_choice == "Да":
                current_number = input("Номер квитанции - ")
                receipts.using_a_receipt(current_number)
            elif our_choice == "Нет":
                user_data = main.Receipt(input("Имя - "), input("Очество - "), input("Фамилия - "), "Техника", "Выдана")
                receipts.using_all_receipts(user_data)
            else:
                print("""Введена не корректная информация в графе "Ваш выбор" """)
                current_choice.getting_choice(current_choice)
        else:
            print("""Введены не корректные данные в графе "Вводные данные(Сдаю в ремонт/Информация)" """)
            self.user_choice = input()
            current_choice.getting_choice(current_choice)


current_choice = Information(input("Вводные данные(Сдаю в ремонт/Информация) - "))
current_choice.getting_choice(current_choice)
